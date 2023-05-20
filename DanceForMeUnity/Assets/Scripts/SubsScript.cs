using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using UnityEngine.Audio;
using System;
using TMPro;
using Unity.VisualScripting;


/// <summary>
/// Used primary for showing the subtitles in accordance to the dialog being played
/// </summary>
public class SubsScript : MonoBehaviour
{
    public Animator animator;
    [SerializeField] TextMeshProUGUI textBox;
    public string[] IntroDialogs = {"Before we start, please read the agreement on screen and nod to confirm the terms of condition!",  "Hey you! Come over here and dance with me.","Stop! Its time to dance!", "Hey you! yeah you. Are you bored of coursework yet? Come over here and dance with me!", "OH MY GOD! IT IS A PERSON! Shut up and dance with me!", "I bet you can't beat the high score!", "Let's break it down. You and me buddy." };
    public string[] IntroAudio = { "T&C", "HEY_YOU_Trial1","TIMETODANCE","BoredCW","ITSAPERSON", "BET","U_N_Me"};
    public string[] IdleDialogs = { "Hmm. I have not seen a single person in hours. Are they all working on their coursework in lab?", "I am bored...Can somebody please dance with me?", "This system will self-destruct if nobody comes over in 10 seconds", "(Sobbing) Where are the students... I miss them..."};
    public string[] IdleAudio = {"I_am_bored_Trial1",  "Not_Seen_Trial1", "Self_Destruct_Trial1", "Sob_Trial1"};
    public string[] DanceMenuDialogs = { "Good choice, I guess...", "NICE!!!", "Come on, we haven't got all day!", "Excellent Choice!", "Man, I just can't wait to get to dancing!", "Oh wow how predictable..." };
    public string[] DanceMenuAudio = {"GoodChoiceIGuess", "NICE","COMEON", "ExcellentChoice", "CANTWAITTODANCE","predictable"};
    public string[] PictureScnenDialogs = { "Woah, who called the paparazzi? You are a SUPERSTAR!", "Smile, you are on camera!!", "Wanna take a pic for the leaderboard? SMILE!" };
    public string[] PictureScnenAudio = {"SUPERSTAR","YOURONCAM","SMILE"};
    
    public string[] ScoreboardDialogs = { "Wow! Do you wanna work with me in the future?", "Wow! Have you ever considered doing this professionally?", "I love your dance, brilliant!!!!" };
    public string[] ScoreboardDialogs1 = { "Ok, let's go back to your coursework....", "Ok, maybe stick to coding...YOU SUCK AT THIS!", "You dance like a robot, and that is coming from a robot!" };
    
    public string[] ScoreboardAudio= {"Work_with_me_in_future","PRO", "Love_ur_dance"};
    public string[] ScoreboardAudio1 = { "CW", "STICKTOCODING", "Dance_like_a_robot" };

    public string[] TutorialDialogs = { "Now lift your right arm to the side.", "Alright, I want you to lift your left arm to the side.","Not bad. Now give me a T-Pose!!","Brilliant! Let's get our boogie on!!"};
    public string[] TutorialAudio = { "RightArm", "LeftArm","TPose","Boogie_On"};


    ///<param name="dialogs">Consists of all the subtitles in the current scene</param>
    ///<param name="audio">Consists of all the audio file names in the current scene</param>
    /// <summary>
    /// This function will run indefinitely until the scene has changed
    /// It will first get a random number, then using the Play() method
    /// from the AudioManager class to play the audio. Then getClipLength()
    /// will be called to obtain the clip's length, which will be used to
    /// determine when the subtitles will be cleared.
    /// </summary>
    IEnumerator sub(string[] dialogs, string[] audio)
    {
        while (true)
        {
            int num = UnityEngine.Random.Range(0, dialogs.Length);
            textBox.text = dialogs[num];
            FindObjectOfType<AudioManager>().Play(audio[num]);
            yield return new WaitForSeconds(FindObjectOfType<AudioManager>().getClipLength(audio[num]));
            textBox.text = "";
            yield return new WaitForSeconds(5);
        }

    }



    /// <summary>
    /// Used to determine which set of subtitles and dialogs to use
    //  in accordance to the scene.
    /// </summary>
    void Start()
    {

        string scene_name = SceneManager.GetActiveScene().name;
        //To determine which set of dialogs to get
        if (scene_name == "IntroMenu")
        {
            StartCoroutine(sub(IntroDialogs, IntroAudio));
        }
        else if (scene_name == "ScoreBoard")
        {
            int inScoreBoard = PlayerPrefs.GetInt("InScoreBoard");
            print(inScoreBoard);
            if (inScoreBoard >= 1)
            {
                StartCoroutine(sub(ScoreboardDialogs, ScoreboardAudio));
            }
            else
            {
                StartCoroutine(sub(ScoreboardDialogs1, ScoreboardAudio1));
            }
        }
        else if (scene_name == "PictureScene")
        {
            StartCoroutine(sub(PictureScnenDialogs, PictureScnenAudio));
        }
        else if (scene_name == "IdleMode")
        {
            StartCoroutine(sub(IdleDialogs,IdleAudio));
        }
        else if (scene_name == "DanceMenuTest")
        {
            StartCoroutine(sub(DanceMenuDialogs, DanceMenuAudio));
        }
        else if (scene_name == "Tutorial")
        {

            StartCoroutine(tutorialAudioSettings(TutorialDialogs, TutorialAudio));
        }
        else if(scene_name == "0DanceScene" || scene_name == "1DanceScene" || scene_name == "2DanceScene")
        {
            string[] MISCDialogs = { "YOU ARE KILLING IT", "YEAH, LET IT RIP", "YEAHHHHHHH!!!", "Work it girlllllll", "SLAYYYYY. Pop off queen", "BREAK IT DOWN!!!", "TRASHHHHHH. GARBAGEEE. DOO DOO WATERRRR.", "My grandma dances better than you ---- DREADFUL"};
            string[] MISCAudio = {"URKILLINGIT","LETITRIP","YEAHHHH","WORKIT","SLAYYYYY","BREAKITDOWN","TRASHHHHHH", "Grandma" };
            StartCoroutine(danceSceneAudioSettings(MISCDialogs, MISCAudio));
        }
    }

    // Update is called once per frame
    void Update()
    {

    }


    
    /// <summary>
    /// This method is used to make sure that the audio array does not move to another index
    /// if the pose that the user has struck is not the correct one. This can be checked using
    /// animator.GetBool. 
    /// </summary>
    ///<param name="dialogs">Consists of all the subtitles in the current scene</param>
    ///<param name="audio">Consists of all the audio file names in the current scene</param>
    IEnumerator tutorialAudioSettings(string[] dialogs, string[] audio)
    {
        int i = 0;
        while (i != 3)
        {
            textBox.text = dialogs[i];
            FindObjectOfType<AudioManager>().Play(audio[i]);
            yield return new WaitForSeconds(FindObjectOfType<AudioManager>().getClipLength(audio[i]));
            textBox.text = "";
            
            if ((i == 0 && animator.GetBool("hasLeftUp")) || (i == 1 && animator.GetBool("hasRightUp")) || (i == 2 && animator.GetBool("hasTPose")))
            {
                ++i;
            }
            yield return new WaitForSeconds(1);
        }
        textBox.text = dialogs[3];
        FindObjectOfType<AudioManager>().Play(audio[3]);
        yield return new WaitForSeconds(FindObjectOfType<AudioManager>().getClipLength(audio[3]));
        textBox.text = "";
    }

    /// <summary>
    /// This method will play the appropriate audio clip according to the player's score.
    /// If it is a bad score, it will play the bad dialog. If it is a good score, it will
    /// play the good dialog.
    /// </summary>
    ///<param name="dialogs">Consists of all the subtitles in the current scene</param>
    ///<param name="audio">Consists of all the audio file names in the current scene</param>
    IEnumerator danceSceneAudioSettings(string[] dialogs, string[] audio)
    {
        while(true)
        {
            if(FindObjectOfType<ScoringSystem>().getCurrentFrameScore() == 1 || FindObjectOfType<ScoringSystem>().getCurrentFrameScore() == 2)
            {
                int num = UnityEngine.Random.Range(6, 8);
                textBox.text = dialogs[num];
                FindObjectOfType<AudioManager>().Play(audio[num]);
                yield return new WaitForSeconds(FindObjectOfType<AudioManager>().getClipLength(audio[num]));
                textBox.text = "";
            }
            else
            {
                int num = UnityEngine.Random.Range(0, 6);
                textBox.text = dialogs[num];
                FindObjectOfType<AudioManager>().Play(audio[num]);
                yield return new WaitForSeconds(FindObjectOfType<AudioManager>().getClipLength(audio[num]));
                textBox.text = "";
            }
            yield return new WaitForSeconds(3);
        }
    }
}


