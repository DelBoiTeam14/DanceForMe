using System.Collections;
using System.IO;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class HighscoreTable : MonoBehaviour {

    private Transform entryContainer;
    private Transform entryTemplate;
    private List<Transform> highscoreEntryTransformList;
    private string chosenDance;
    private string path;
    private string filePath;

    private void Awake() {
       // PlayerPrefs.DeleteAll();
        filePath = Application.dataPath + "/PlayersImages/";

        chosenDance = PlayerPrefs.GetInt("ChosenDance").ToString();
        int scores = PlayerPrefs.GetInt("HighScore");
        path = "highscoreTable_" + chosenDance;
        FindObjectOfType<ChangeScene>().callStart(13,"IdleMode");
        entryContainer = transform.Find("highscoreEntryContainer");
        entryTemplate = entryContainer.Find("highscoreEntryTemplate");
        entryTemplate.gameObject.SetActive(false);
        string jsonString = PlayerPrefs.GetString(path);
        Highscores highscores = JsonUtility.FromJson<Highscores>(jsonString);

        if(highscores != null)
        {
            int entries = highscores.highscoreEntryList.Count;
            Debug.Log(PlayerPrefs.GetString(path) + entries);
            
            // Sort entry list by Score
            for (int i = 0; i < entries; i++)
            {
                for (int j = i + 1; j < entries; j++)
                {
                    if (highscores.highscoreEntryList[j].score > highscores.highscoreEntryList[i].score)
                    {
                        // Swap
                        HighscoreEntry tmp = highscores.highscoreEntryList[i];
                        highscores.highscoreEntryList[i] = highscores.highscoreEntryList[j];
                        highscores.highscoreEntryList[j] = tmp;
                    }
                }
            }
            //Remove all entries that are not in top 5
            int counter = 0;
            highscoreEntryTransformList = new List<Transform>();
            for (int i = 0; i < entries; i++)
            {
                HighscoreEntry highscoreEntry = highscores.highscoreEntryList[i];
                counter = counter + 1;
                // if (counter >= 5)
                // {
                //     Debug.Log(highscoreEntry.name);
                //     highscores.highscoreEntryList.Remove(highscoreEntry);
                //     //remove image 
                //     string finalPath = filePath + highscoreEntry.name;
                //     if (File.Exists(finalPath))
                //     {
                //         File.Delete(finalPath);
                //     }
                //     // break;
                //     string json = JsonUtility.ToJson(highscores);
                //     PlayerPrefs.SetString(path, json);
                //     PlayerPrefs.Save();
                // }
                // else
                // {
                    if(counter < 5){
                    CreateHighscoreEntryTransform(highscoreEntry, entryContainer, highscoreEntryTransformList);
                    }
                // }
            }
            //foreach (HighscoreEntry highscoreEntry in highscores.highscoreEntryList)
            //{
            //    counter = counter + 1;
            //    if (counter >= 5)
            //    {
            //        Debug.Log(highscoreEntry.name);
            //        highscores.highscoreEntryList.Remove(highscoreEntry);
            //        //remove image 
            //        string finalPath = filePath + highscoreEntry.name;
            //        if (File.Exists(finalPath)) {
            //            File.Delete(finalPath);
            //        }
            //        // break;
            //        string json = JsonUtility.ToJson(highscores);
            //        PlayerPrefs.SetString(path, json);
            //        PlayerPrefs.Save();
            //    }
            //    else {
            //        CreateHighscoreEntryTransform(highscoreEntry, entryContainer, highscoreEntryTransformList);
            //    }
            //}

        }

    }

    private void CreateHighscoreEntryTransform(HighscoreEntry highscoreEntry, Transform container, List<Transform> transformList) {
        float templateHeight = 50f;
        Transform entryTransform = Instantiate(entryTemplate, container);
        RectTransform entryRectTransform = entryTransform.GetComponent<RectTransform>();
        entryRectTransform.anchoredPosition = new Vector2(0, -2 * templateHeight * transformList.Count);
        entryTransform.gameObject.SetActive(true);

        int rank = transformList.Count + 1;
        string rankString;
        switch (rank) {
        default:
            rankString = rank + "TH"; break;

        case 1: rankString = "1ST"; break;
        case 2: rankString = "2ND"; break;
        case 3: rankString = "3RD"; break;
        }

        entryTransform.Find("posText").GetComponent<Text>().text = rankString;

        int score = highscoreEntry.score;
        string winnerPath = highscoreEntry.name;

        entryTransform.Find("scoreText").GetComponent<Text>().text = score.ToString();
        
        string imagePath = "Assets/PlayersImages/" + winnerPath;
        if (File.Exists(imagePath))
        {
            Texture2D texture = LoadTextureFromFile(imagePath);
            // Create a sprite from the loaded texture
            Sprite sprite = Sprite.Create(texture, new Rect(0, 0, texture.width, texture.height), Vector2.one * 0.5f);
            entryTransform.Find("Mask").transform.GetChild(0).GetComponent<Image>().sprite = sprite;
        }

        // Highlight First
        if (rank == 1) {
            entryTransform.Find("posText").GetComponent<Text>().color = Color.green;
            entryTransform.Find("scoreText").GetComponent<Text>().color = Color.green;
        }

        transformList.Add(entryTransform);
    }

    private class Highscores {
        public List<HighscoreEntry> highscoreEntryList;
    }

    /*
     * Represents a single High score entry
     * */
    [System.Serializable] 
    private class HighscoreEntry {
        public int score;
        public string name;
    }

Texture2D LoadTextureFromFile(string filePath)
{
    // Load the texture data from the file
    byte[] fileData = File.ReadAllBytes(filePath);

    // Create a new texture and load the image data into it
    Texture2D texture = new Texture2D(2, 2);
    texture.LoadImage(fileData);

    return texture;
}
}
