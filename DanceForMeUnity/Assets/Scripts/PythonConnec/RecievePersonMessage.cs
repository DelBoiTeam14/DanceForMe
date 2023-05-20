using System.Collections;
using System.Collections.Generic;
using System;
using UnityEngine;
using UnityEngine.SceneManagement;
using TMPro;
public class RecievePersonMessage : MonoBehaviour
{
    public OSC osc;
    string sceneName;
    public Animator animator;
    public TextMeshProUGUI text;
    int i = 0;

    // Use this for initialization
    void Start()
    {
        Scene scene = SceneManager.GetActiveScene();
        sceneName = scene.name;
        print(sceneName);
        osc.SetAddressHandler("/UserDetected", OnReceivePersonDetected);
    }

    // Update is called once per frame
    void Update()
    {

    }

    void OnReceivePersonDetected(OscMessage message)
    {
        string x = message.GetString(0);        

        if (sceneName == "IdleMode")
        {
            if (x == "T-POSE") {
                FindObjectOfType<ChangeScene>().callStart(2, "IntroMenu");
            }
        }
        else if (sceneName == "IntroMenu" && x == "T-POSE")
        {
            FindObjectOfType<ChangeScene>().callStart(2, "Tutorial");
        }
        else if( sceneName == "Tutorial")
        {     
            if (i == 0)
            {

                if (x == "RIGHT")
                {
                    Debug.Log("RIGHT DETECCTED");

                    animator.SetBool("hasLeftUp", true);
                    i++;

                }
                else
                {
                    animator.SetBool("hasLeftUp", false);

                }


            }
            if (i == 1)
            {
                if (x == "LEFT")
                {
                    Debug.Log("LEFT DETECCTED");

                    animator.SetBool("hasRightUp", true);
                    i++;
                }
                else
                {
                    animator.SetBool("hasRightUp", false);
                }

            }
            if (i == 2) {

                if (x == "TPOSE")
                {
                    Debug.Log("TPOSE DETECCTED");
                    i++; 
                    animator.SetBool("hasTPose", true);
                }
                else {

                    animator.SetBool("hasTPose", false);

                }

            }

            if (i == 3) {

                FindObjectOfType<ChangeScene>().callStart(7, "DanceMenu");
            }
        }
    
        
     }
    


}
