using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

///<summary>
/// <c>ChangeImage</c> class is used to change the sprite of the oldImage object
///</summary>
public class ChangeImage : MonoBehaviour
{
    public Image oldImage;
    public Sprite on;
    public Sprite off;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    
    /// <summary>
    /// Changes the sprite of the "oldImage" object to the opposite sprite. 
    /// </summary>
    /// <remarks>
    /// Changes the sprite of the "oldImage" object to "off" if it's currently "on", and vice versa.
    /// </remarks>
    public void ImageChange(){

        if(oldImage.sprite == on){
            oldImage.sprite = off;
        }else if(oldImage.sprite == off){
            oldImage.sprite = on;
        }
        
    }
}
