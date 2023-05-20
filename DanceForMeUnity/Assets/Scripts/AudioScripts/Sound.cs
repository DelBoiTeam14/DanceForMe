using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Audio;
//Sound
//@Description: Used in the form of an array in AudioManager class
//              You can set the name, volume, and pitch of an audio clip
//              using this class
[System.Serializable]
public class Sound
{
    public AudioClip clip;
    public string name;
    [Range(0f, 1f)]
    public float volume;
    [Range(.1f, 3f)]
    public float pitch;
    [HideInInspector]
    public AudioSource source;
}
