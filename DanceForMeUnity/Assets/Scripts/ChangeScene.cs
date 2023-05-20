using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;


/// <summary>
/// Class <c>ChangeScene</c> changes scene with a time delay
/// </summary>
public class ChangeScene : MonoBehaviour
{
    [SerializeField]
    public string SceneName;
    void Update() {
        if (Input.GetKeyDown(KeyCode.N))
        {
            Initiate.Fade(SceneName, Color.black, 1f);
        }
    
    }


private void Awake()
    {
         //Set screen size for Standalone
        #if UNITY_STANDALONE
           Screen.SetResolution(1920 , 1080, true);
        #endif

    }

    /// <summary>
    /// Moves to a specified scene after a delay.
    /// </summary>
    /// <param name="time">The delay time in seconds.</param>
    /// <param name="scene">The name of the scene to move to.</param>
    /// <remarks>
    /// This method is used to move to a specified scene from another C# file, since it's not possible to call an IEnumerator function from other C# files.
    /// </remarks>
    public void callStart(int time, string scene)
    {
        StartCoroutine(MoveToScene(time,scene));
    }

    /// <summary>
    /// Changes to a specified scene after a certain amount of time has passed.
    /// </summary>
    /// <param name="time">The delay time in seconds.</param>
    /// <param name="scene">The name of the scene to change to.</param>
    /// <remarks>
    /// This method is used to change to a specified scene after a certain amount of time has passed.
    /// </remarks>
    public IEnumerator MoveToScene(int time,string scene)
    {
        yield return new WaitForSeconds(time);
        Initiate.Fade(scene, Color.black, 1f);

    }

}
