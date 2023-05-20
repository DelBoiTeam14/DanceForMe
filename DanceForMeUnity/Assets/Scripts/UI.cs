using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;

namespace ui
{
    public class UI : MonoBehaviour
    {
        [SerializeField] TextMeshProUGUI subtitleText = default;

        public static UI instance;

        /// Sets the value of the variable instance to the current instance of the script
        ///</summary>
        private void Awake()
        {
            instance = this;
        }

        //@SetSubtitle()
        //@Description: Sets the subtitle text in the UI
        //@Param: string subtitle - the text to be set as the subtitle
        ///<summary>
        /// Sets the subtitle text in the UI.
        ///</summary>
        ///<param name="subtitles">a string that needs to be displayed by the UI</param>
        public void SetSubtitle(string subtitle)
        {
            subtitleText.text = subtitle;
        }
    }
}
