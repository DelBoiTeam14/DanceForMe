using System.Collections;
using System.Collections.Generic;
using System.IO;
using System;
using System.Text;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
using UnityEngine.SceneManagement;
using Random = UnityEngine.Random;

public class Scoring : MonoBehaviour
{
    public TextMeshProUGUI ScoreText;
    public int score { get; set; }
    public int maxScore;
    public bool end = false;
    [SerializeField]
    public Animator TextAnimator;
    [SerializeField]
    public Animator animator;
    [SerializeField]
    public TextMeshProUGUI feedbackText;
    [SerializeField]
    public ScoreBar scoreBar;
    private string chosenDance;
    private string filePath;
    private string path;
    [SerializeField] 
    private bool done = false;
    private List<Transform> highscoreEntryTransformList;

    // Start is called before the first frame update
    void Start()
    {

        chosenDance = PlayerPrefs.GetInt("ChosenDance").ToString();
        filePath = Application.dataPath + "/PlayersImages/";
        path = "highscoreTable_" + chosenDance;
        score = 0;
        scoreBar.SetScore(score);
    }

    /// <summary>
    /// It checks whether the score variable being passed in is equal or higher than the current top 5 highest score.
    /// </summary>
    /// <param name="score">The score variable to check</param>
    /// <returns>true if the score is equal to or higher than the top 5 highest score, otherwise false.</returns>
    bool checkTopScore(int score)
    {
        string jsonString = PlayerPrefs.GetString(path);
        Highscores highscores = JsonUtility.FromJson<Highscores>(jsonString);
        if (highscores != null)
        {
            for (int i = 0; i < highscores.highscoreEntryList.Count; i++)
            {
                for (int j = i + 1; j < highscores.highscoreEntryList.Count; j++)
                {
                    if (highscores.highscoreEntryList[j].score > highscores.highscoreEntryList[i].score)
                    {
                        HighscoreEntry tmp = highscores.highscoreEntryList[i];
                        highscores.highscoreEntryList[i] = highscores.highscoreEntryList[j];
                        highscores.highscoreEntryList[j] = tmp;
                    }
                }
            }

            for (int j = 0; j < highscores.highscoreEntryList.Count; j++)
            {
                if (score >= highscores.highscoreEntryList[j].score)
                    return true;
                
            }
            return false;
        }

        return true;
    }



    private void AddHighscoreEntry(int score, string name)
    {
        PlayerPrefs.SetString("winnerPath", name);
        PlayerPrefs.Save();

        // Create HighscoreEntry
        HighscoreEntry highscoreEntry = new HighscoreEntry { score = score, name = name };
        // Load saved Highscores
        string jsonString = PlayerPrefs.GetString(path);
        Highscores highscores = JsonUtility.FromJson<Highscores>(jsonString);

        if (highscores == null)
        {
            // There's no stored table, initialize
            highscores = new Highscores()
            {
                highscoreEntryList = new List<HighscoreEntry>()
            };
        }

        // Add new entry to Highscores
        highscores.highscoreEntryList.Add(highscoreEntry);

        // Save updated Highscores
        string json = JsonUtility.ToJson(highscores);
        PlayerPrefs.SetString(path, json);
        PlayerPrefs.Save();
    }




    private class Highscores {
        public List<HighscoreEntry> highscoreEntryList;
    }

    [System.Serializable] 
    private class HighscoreEntry {
        public int score;
        public string name;
    }

    /// <summary>
    /// Checks whether the dance has ended by calling getEnded() from SongsForDance class.
    /// If the dance has ended, it will call appendScoreToFile() to find out whether the current score
    /// is a high score, using checkTopScore(). If it's a high score, it will take the user to the PictureScene
    /// to take a picture. If not, it will take the user to the ScoreBoard.
    /// </summary>
    void Update()
    {
        UpdateScoreUI();
        if (!done && animator.GetCurrentAnimatorStateInfo(0).normalizedTime > 1 && !animator.IsInTransition(0))
        {
            bool inScoreBoard = checkTopScore(score);
            if (inScoreBoard)
            {
                PlayerPrefs.SetInt("HighScore", score);
                PlayerPrefs.SetInt("InScoreBoard", 1);
                int randomNumber = Random.Range(1, 5);
                string winnerPath = "game" + chosenDance.ToString() + "/" + score.ToString() + "_" + randomNumber.ToString() + ".png";
                print("hello you win" + winnerPath);
                AddHighscoreEntry(score,  winnerPath);
                done = true;
                FindObjectOfType<ChangeScene>().callStart(1, "PictureScene");

            }
            else
            {
                
                PlayerPrefs.SetInt("InScoreBoard", 0);
                done = true;
                FindObjectOfType<ChangeScene>().callStart(1, "ScoreBoard");
                
            }

        }
    }


    /// <summary>
    /// Add the newScore to the current score. Then pass in the current score
    /// to the scoreBar so it can update the visual. Then ShowFeedbackText() will be called
    /// to show the feedback according to the newScore
    /// </summary>
    /// <param name="newScore">The new score to add to the current score</param>
    public void AddScore(int newScore)
    {
        score += newScore;
        scoreBar.SetScore(score);
        ShowFeedbackText(newScore);
    }

    /// <summary>
    /// Shows feedback text based on the new score.
    /// </summary>
    /// <param name="newScore">The new score that will determine the feedback text to be displayed.</param>
    /// <remarks>
    /// This function is a helper function for AddScore().
    /// </remarks>
    public void ShowFeedbackText(int newScore) {

           if (newScore >= 5)
            {
                feedbackText.text = "NICE!";
                feedbackText.color = Color.magenta;
                feedbackText.GetComponent<Animator>().SetTrigger("Change");
                //feedbackText.text = "";
            }
            else if (newScore >= 2)
            {
                feedbackText.text = "OKAY";
                feedbackText.color = Color.cyan;
                feedbackText.GetComponent<Animator>().SetTrigger("Change");
                //feedbackText.text = "";

            }
            else
            {
                feedbackText.text = "BAD";
                feedbackText.color = Color.white;
                feedbackText.GetComponent<Animator>().SetTrigger("Change");
                //feedbackText.text = "";

            }
    }

    /// <summary>
    /// Updates the score text on screen.
    /// </summary>
    public void UpdateScoreUI()
    {
        ScoreText.text = "Score  " + score;
    }

}
