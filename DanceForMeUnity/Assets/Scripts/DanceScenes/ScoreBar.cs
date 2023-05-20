using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;


/// <summary>
/// Class <c>ScoreBar</c> shows the score bar during the dance scene
/// </summary>
public class ScoreBar : MonoBehaviour
{
    public Slider slider;
    public Gradient gradient;
    public Image fill;

    /// <summary>
    /// Sets the score value of the slider and fills the score bar accordingly.
    /// </summary>
    /// <param name="newScore">The new score to set the slider value to.</param>
    public void SetScore(int newScore) {
        slider.value = newScore;
        fill.color = gradient.Evaluate(slider.normalizedValue);
    }
}
