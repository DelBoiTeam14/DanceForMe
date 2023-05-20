using System;
using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.Audio;

//@AudioManager
//@Description: Used for audio related operations.
public class AudioManager : MonoBehaviour
{
    public Sound[] sounds;
    
    //@Awake()
    //@Description: Activated when the scene is called and act as a constructor
    //              for the AudioManager class
    void Awake()
    {
        //Initializing the Sound object 
        foreach (Sound s in sounds)
        {
            s.source = gameObject.AddComponent<AudioSource>();
            s.source.clip = s.clip;
            s.source.volume = s.volume;
            s.source.pitch = s.pitch;
        }
    }

    //@getClipLength()
    //@Param: string name (file name)
    //@Description: It will find the file name within the sounds array using the 
    //              argument being passed in. Then it will return the length of the
    //              clip
    //@return: The length of the clip (int)
    public int getClipLength(string name)
    {
        Sound s = Array.Find(sounds, sound => sound.name == name);
        return (int)s.source.clip.length;
    }

    //@Play()
    //@Param: string name (file name)
    //@Description: It will find the file name within the sounds array using the 
    //              argument being passed in. Then if the file is found, it will play the
    //              audio clip.
    public void Play(string name)
    {
        //Finding the audio clip with the name, if it fails to obtain the clip, an error will be shown
        Sound s = Array.Find(sounds, sound => sound.name == name);
        //play the audio source
        s.source.Play();
        
    }

    //@Mute()
    //@Description: It will set the volume to 0 for all the elements within the sounds array.
    public void Mute()
    {
        foreach (Sound s in sounds)
        {
            s.source.volume = 0;
            s.source.pitch = 0;
        }
    }
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}

