using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;


public class WobblyText : MonoBehaviour
{
    public TMP_Text textComponent;

    // Update is called once per frame
    void Update()
    {

        textComponent.ForceMeshUpdate(); //makes sure meshes used my TMP are upto date
        var textInfo = textComponent.textInfo; //saves whats in the text
        for(int i = 0; i < textInfo.characterCount; ++i){
            var charInfo = textInfo.characterInfo[i]; //saves character in an array

            if(!charInfo.isVisible){//skip any invisible characters
                continue; 
            }

            var verts = textInfo.meshInfo[charInfo.materialReferenceIndex].vertices; //save the vert info of the current character
//update draft copy
            for(int j = 0; j <4; ++j){ //a loop for each vertices of the character , store current position of vertex
                var orig = verts[charInfo.vertexIndex + j]; //the unchanged version 
                verts[charInfo.vertexIndex + j] = orig + new Vector3(0, Mathf.Sin(Time.time*2f+orig.x*0.01f)* 10f, 0); //overwrite with a modified version
            }
        }
        //update working copy
        for(int i=0; i <textInfo.meshInfo.Length; ++i){
            var meshInfo = textInfo.meshInfo[i];
            meshInfo.mesh.vertices = meshInfo.vertices;
            textComponent.UpdateGeometry(meshInfo.mesh, i);
        }


    }
}
