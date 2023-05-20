using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using System.Threading;
using System.Text;


/// <summary>
/// Class <c>ToCwindow</c> uses to show a pop up window on the screen.
/// </summary>
public class ToCwindow : MonoBehaviour
{
    [SerializeField] public PopUpWindow termsCondWindow;
    public OSC osc;
    public AudioSource source;
    public AudioClip clip;


    // Serialise field lets us see it in the inspector in unity
    public bool isVisible = false;

    ///<summary>
    /// Invokes the "OpenTermsWindow" method after 5 seconds and sets an address handler for "/PoseDetection" on the osc object
    ///</summary>
    void Start(){
        Invoke("OpenTermsWindow", 3);
        osc.SetAddressHandler("/PoseDetection", OnReceivePersonDetected);
    }

    ///<summary>
    /// This function will set the PopUpWindow object as active,
    /// then play an audio that goes with the window being popped up.
    /// Then the appropriate text will show up with the window according to the scene
    ///</summary>
    private void OpenTermsWindow (){

        isVisible = true;
        termsCondWindow.gameObject.SetActive(isVisible);
        source.PlayOneShot(clip);
        string sceneName = SceneManager.GetActiveScene().name;
        termsCondWindow.confirmButton.onClick.AddListener(UserConfirm);
        if (sceneName == "IntroMenu")
        {
            termsCondWindow.messageText.text = "The user allows the system to record an image of the user which is stored in a database. The user takes responsibility for any injury or damage caused while using this system and should be always aware of their surroundings. ";
        }
        else if (sceneName == "Tutorial")
        {
            termsCondWindow.messageText.text = "Are you still with us?";
        }
     
    }

    ///<summary>
    /// It will load the appropriate scene according to the message being sent
    /// from the python script to C#
    /// </summary>
    ///<param name="message">message is an OscMessage object</param>
    void OnReceivePersonDetected(OscMessage message)
    {
        string x = message.GetString(0);
        string name = SceneManager.GetActiveScene().name;

        if (x == "NOD" &&  name == "IntroMenu")
        {

            SceneManager.LoadScene("Tutorial");

        }
        else if (x == "" && name == "Tutorial")
        {
            SceneManager.LoadScene("IdleMode");

        }
        else if (x == "NOD" && name == "Tutorial")
        {
            SceneManager.LoadScene("DanceMenuTest");

        }
    }

    ///<summary>
    /// This will set isVisible variable to false, also the 
    /// pop window will no longer be visible.
    ///</summary>
    private void UserConfirm(){
        isVisible = false;
        termsCondWindow.gameObject.SetActive(false);
    }


}
