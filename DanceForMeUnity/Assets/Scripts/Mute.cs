using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Mute : MonoBehaviour
{
    ///<summary>
    /// Toggles the mute state of the AudioListener. Sets the volume of the AudioListener to 1 if mute is true,
    /// and 0 if it's false.
    ///</summary>
    /// <param name="mute">Indicates whether or not the the AudioListener should be muted</param>
    public void MuteToggle(bool mute)
    {
      if(AudioListener.volume == 0){
          AudioListener.volume = 1;
      }
      else
      {
          AudioListener.volume = 0;
      }
    }
}
