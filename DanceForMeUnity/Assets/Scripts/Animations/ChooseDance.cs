using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using DanielLochner.Assets.SimpleScrollSnap;
using UnityEngine.SceneManagement;
using UnityEngine.UI;
using System.IO;


public class ChooseDance : MonoBehaviour
{
    public OSC osc;
    public int current;
    SimpleScrollSnap simpleScrollSnap;
    [SerializeField] private GameObject menu;
    [SerializeField] private GameObject content;

    private GameObject danceChoice;
    private Text scores;
    private string mainPath;
    private class Highscores
    {
        public List<HighscoreEntry> highscoreEntryList;
    }

    [System.Serializable]
    private class HighscoreEntry
    {
        public int score;
        public string name;
    }

    public void Awake()
    {
        simpleScrollSnap = menu.GetComponent<SimpleScrollSnap>();
        mainPath = Application.dataPath;
    }
    public void getCurrentDance()
    {
   

        this.current = simpleScrollSnap.CenteredPanel;
        PlayerPrefs.SetInt("ChosenDance", this.current);
        PlayerPrefs.Save();
        FindObjectOfType<ChangeScene>().callStart(0, current.ToString() + "DanceScene");

    }

    // Start is called before the first frame update
    void Start()
    {
        osc.SetAddressHandler("/DanceMenu", onRecieveMessage);
        LoadHighScore();

    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.RightArrow))
        {
            // Left arrow key is pressed
            simpleScrollSnap.GoToNextPanel();

        }
        else if (Input.GetKeyDown(KeyCode.LeftArrow))
        {
            // Right arrow key is pressed
            simpleScrollSnap.GoToPreviousPanel();

        }
    }

    public void onRecieveMessage(OscMessage message) {


        string x = message.GetString(0);
        Debug.Log(x);
        if (x == "T-POSE")
        {
            getCurrentDance();
            
        }
        else if (x == "RIGHT")
        {
            simpleScrollSnap.GoToNextPanel();
        }
        else if (x == "LEFT")
        {
            simpleScrollSnap.GoToPreviousPanel();
        }
    }

    private IEnumerator LoadSceneAsync()
    {
        AsyncOperation asyncLoad = SceneManager.LoadSceneAsync("DanceScene", LoadSceneMode.Single);

        while (!asyncLoad.isDone)
        {
            yield return null;
        }

        this.current = simpleScrollSnap.CenteredPanel;
        PlayerPrefs.SetInt("ChosenDance", this.current);
    }

    public string getHighestScore(int danceScene)
    {
        string jsonString = PlayerPrefs.GetString("highscoreTable_"+ danceScene.ToString());
        int highestScore = 0;
        string path = "";
        if (jsonString != "")
        {
            print(jsonString);
            Highscores highscores = JsonUtility.FromJson<Highscores>(jsonString);
            print(highscores);


            for (int i = 0; i < highscores.highscoreEntryList.Count; i++)
            {
                int currScore = highscores.highscoreEntryList[i].score;
                if (currScore > highestScore)
                {
                    highestScore = currScore;
                    path = highscores.highscoreEntryList[i].name;
                }

            }
        }
        return path;

    }

    void LoadHighScore() {
        GameObject winner;
        GameObject scores;

        for (int i = 0; i < content.transform.childCount; i++)
        {
            danceChoice = content.transform.GetChild(i).gameObject;
            winner = danceChoice.transform.GetChild(0).transform.GetChild(0).gameObject;
            scores = danceChoice.transform.GetChild(1).gameObject;
            string highest_scores = getHighestScore(i);
            print(highest_scores);
            string pic_path = "Assets/PlayersImages/" + highest_scores;
            if (File.Exists(pic_path))
            {
                Texture2D texture = LoadPNG(pic_path);
                Image img = winner.GetComponent<Image>();
                img.sprite = TextureToSprite(texture);
                scores.GetComponent<TMPro.TextMeshProUGUI>().text = "Scores: " + highest_scores;

            }
            else
            {
                scores.GetComponent<TMPro.TextMeshProUGUI>().text = "Scores: - ";
            }

        }

    }

    public static Texture2D LoadPNG(string filePath)
    {
        Texture2D texture = null;
        byte[] fileData;
        if (File.Exists(filePath))
        {
            print("Image loaded");
            fileData = File.ReadAllBytes(filePath);
            texture = new Texture2D(2, 2);
            texture.LoadImage(fileData);
        }
        return texture;
    }

    public static Sprite TextureToSprite(Texture2D texture)
    { 
        Sprite newSprite = Sprite.Create(texture, new Rect(0f, 0f, texture.width, texture.height),
            new Vector2(0.5f, 0.5f), 100);
        return newSprite;
    }
}
