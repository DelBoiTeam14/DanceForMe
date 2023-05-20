using System;
using System.Diagnostics;
using System.Collections;
using System.Collections.Generic;
using System.Threading.Tasks;
using UnityEngine;
using UnityEngine.SceneManagement;



/// <summary>
/// Class <c>SongsForDance</c> uses to play audio(songs) for the dancing part of the system
/// </summary>
public class SongsForDance : MonoBehaviour
{
    Stopwatch stopwatch = new Stopwatch();

    public AudioSource source;
    public AudioClip[] clip;
    public bool ended = false;

    /// <summary>
    /// Retrieves the selected dance option from the game settings.
    /// </summary>
    /// <returns> An integer representing the selected dance option. 0 = Computer Science, 1 = Ballet, 2 = Cowboy.</returns>
    int getDance()
    {
        // Process process = new Process();

        // // Set the process start information
        // process.StartInfo.FileName = "../BatFiles/DanceScene.bat";
        // process.StartInfo.Arguments = PlayerPrefs.GetInt("ChosenDance").ToString(); // Pass the data as command-line argument
        // process.StartInfo.UseShellExecute = false;
        // process.StartInfo.RedirectStandardOutput = true;

        // // Start the process
        // process.Start();
        return PlayerPrefs.GetInt("ChosenDance");
    }

    /// <summary>
    /// Retrieves the value of the "ended" variable.
    /// </summary>
    /// <returns>A boolean indicating whether the "ended" variable is true or false.</returns>
    public bool getEnded()
    {
        return ended;
    }


    void Start()
    {
        stopwatch.Start();
        playSong();
    }

    /// <summary>
    /// Loads an audio clip to a source object and plays it.
    /// </summary>
    /// <remarks>
    /// This function loads an audio clip to the source object and plays it using the source.Play() method.
    public void playSong()
    {

        source.clip = clip[getDance()];
        source.Play();
    }

    /// <summary>
    /// Sets the value of the boolean variable ended, depending on the state of the source object.
    /// If the source is no longer playing, ended is set to true, otherwise it's set to false.
    /// </summary>
    /// <remarks>
    /// This method is typically called by an event or coroutine that checks the state of the audio source.
    /// </remarks>
    public void songEnded()
    {

       if(stopwatch.Elapsed.TotalSeconds > 45)
        { 

            ended = true;
            
        }
        
    }

    void Update()
    {
        songEnded();
    }
}
