using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class CountDownTimer : MonoBehaviour
{
    float currentTime = 0;
    [SerializeField] float startTime;
    [SerializeField] TextMeshProUGUI countDownText;

    // Start is called before the first frame update
    void Start()
    {
        currentTime = startTime;
    }

    // Update is called once per frame
    void Update()
    {
        currentTime -= 1 * Time.deltaTime; // Update time each second
        countDownText.text = currentTime.ToString("0");

        if (currentTime < 1) {
            //danceChoice.loadDance();
            Destroy(gameObject, 0);
        }
    }
}
