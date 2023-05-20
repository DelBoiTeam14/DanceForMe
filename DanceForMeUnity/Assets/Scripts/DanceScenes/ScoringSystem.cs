using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
public class ScoringSystem : MonoBehaviour
{
    public Scoring score;
    public OSC osc;
    private int currentFrameScore;
    // Start is called before the first frame update
    void Start()
    {
        osc.SetAddressHandler("/UserDetected", OnReceivePersonDetected);
    }

    void OnReceivePersonDetected(OscMessage message)
    {
        int x = message.GetInt(0);
        // if(x == 5){
        //     x+= 1000000;
        // }
        score.AddScore(x);
        currentFrameScore = x;
    }
    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.P))
        {
            score.AddScore(1);
            currentFrameScore = 1;
        }
        else if (Input.GetKeyDown(KeyCode.I))
        {
            score.AddScore(2);
            currentFrameScore = 2;
        }
        else if (Input.GetKeyDown(KeyCode.O))
        {
            score.AddScore(4);
            currentFrameScore = 4;
        }
    }

    public int getCurrentFrameScore()
    {
        return currentFrameScore;
    }
}
