using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MusicSaver : MonoBehaviour
{

    ///<summary>
    ///Calls the "Don'tDestroyOnLoad" method to prevent the game object from being destroued when a new scene is loaded.
    ///</summary>
    void Start()
    {
        DontDestroyOnLoad(gameObject);//saves the parent and all their child 
    }

}
