using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.IO;
using System.Threading;
using UnityEngine.SceneManagement;


/// <summary>
/// Class <c>TakePicture</c> open webcam and take a image and store in the PlayersImage 
/// </summary>
public class TakePicture : MonoBehaviour
{
    [SerializeField]
    private GameObject WebcamPlane;
    [SerializeField]
    private UnityEngine.UI.RawImage rawImage;
    [SerializeField]
    private UnityEngine.UI.Image circleImage;
    [SerializeField]
    private Image photoDisplay;
    [SerializeField]
    private GameObject frame;
    [SerializeField]
    private Animator fadingAnimation;
    [SerializeField]
    private AudioSource cameraAudio;

    private WebCamTexture camTexture;
    private Texture2D croppedImage;
    private int posX;
    private int posY;
    private int scores;
    private string path;
    void Start()
    {
        path = Application.dataPath + "/PlayersImages/";

        WebCamDevice[] devicesList = WebCamTexture.devices;
        if (devicesList.Length > 0)
        {
            print("Device found with " + devicesList[0].name);
            // assuming the first available WebCam is desired
            camTexture = new WebCamTexture(devicesList[0].name);
            this.rawImage.texture = camTexture;
            camTexture.Play();
            posX = (int)this.circleImage.transform.localPosition.x;
            posY = (int)this.circleImage.transform.localPosition.y;
            // ensure the camera is initialized , invoke take picture function after 3 seconds
            StartCoroutine(TakeImage());
        }
        else {
             Debug.Log("No Camera found");
            FindObjectOfType<ChangeScene>().callStart(2, "ScoreBoard");

        }

    }
    // Update is called once per frame
    void Update()
    {
        //right click to take image
        if (Input.GetMouseButtonDown(0))
        {
            StartCoroutine(TakeImage());
            camTexture.Stop();
            FindObjectOfType<ChangeScene>().callStart(2, "ScoreBoard");
        }
        
    }

    /// <summary>
    /// Captures a picture from the camera and crops it to a specific size.
    /// </summary>
    /// <returns>An IEnumerator that waits for 6 seconds, captures the picture, crops it, and shows it.</returns>
    /// <remarks>
    /// This method captures a picture from the camera and crops it to a size of 500x500 pixels.
    /// </remarks>
    IEnumerator TakeImage()
    {
        yield return new WaitForSeconds(5f);
        int width = camTexture.width;
        int height = camTexture.height;
        Texture2D pic = new Texture2D(width, height);
        pic.SetPixels(camTexture.GetPixels());

        print(height + " " + posX + " "+ width + " "+posY);
        CropImage(pic,width / 2 - 300 , height/4 + 40, 400, 400);
        SaveImage();
        ShowPic();
    }

    void CropImage(Texture2D pic,int x, int y, int width, int height) {
        print("Cropping...");
        croppedImage = new Texture2D(width, height);
        // copy the pixels from the original image to the cropped image
        croppedImage.SetPixels(pic.GetPixels(x, y, width, height));
        croppedImage.Apply();
    }

    IEnumerator FlashEffect() {
        yield return new WaitForSeconds(2f);
        cameraAudio.Play();

    }


    /// <summary>
    /// Saves the cropped image to the player's file system. It gets the current high score and chosen dance from
    /// the PlayerPrefs and encodes the cropped image into PNG format. It then creates a file path with the chosen dance
    /// and high score values as the file name and saves the image to that location.
    /// </summary>
    void SaveImage() {
        int score = PlayerPrefs.GetInt("HighScore");
        int chosenDance = PlayerPrefs.GetInt("ChosenDance");
        byte[] dataToSave = croppedImage.EncodeToPNG();
        string filePath = path + PlayerPrefs.GetString("winnerPath");
        print(filePath);
        //string filePath = Application.dataPath + "/PlayersImages/"+ "game"+ chosenDance.ToString() + "/"+ score.ToString() + ".png";

        File.WriteAllBytes(filePath, dataToSave);
    }

    /// <summary>
    /// This function shows the picture taken from the webcam on the screen.
    /// It creates a sprite from the croppedImage, sets it as the sprite of the photoDisplay object,
    /// disables the WebcamPlane and enables the frame, plays the fading animation and then invokes
    /// the LoadNextScene() function after 3 seconds.
    /// </summary>
    void ShowPic() {
        StartCoroutine(FlashEffect());
        Sprite photoSprite = Sprite.Create(croppedImage,new Rect(0.0f, 0.0f, 400, 400),new Vector2(0.5f,0.5f),100);
        photoDisplay.sprite = photoSprite;
        WebcamPlane.SetActive(false);
        frame.SetActive(true);
        fadingAnimation.Play("Fade");
        Invoke("LoadNextScene", 3f);
    }


    void LoadNextScene() {
        camTexture.Stop();
        FindObjectOfType<ChangeScene>().callStart(2, "ScoreBoard");

    }

    void RemovePic() {
        frame.SetActive(false);
    }
}
