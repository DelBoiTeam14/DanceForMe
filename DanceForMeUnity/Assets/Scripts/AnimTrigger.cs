using System.Collections;
using System.Collections.Generic;
using UnityEngine;

///<summary>
/// <c>AnimTrigger</c> is used for triggering the animator in the current scene.
///</summary>
public class AnimTrigger : MonoBehaviour
{
    private Animator animator;

    /// <summary>
    /// Store the Animator game object to variable animator 
    /// </summary>
    /// <remarks>
    /// the Animator game object has to be set manually from the unity editor
    /// </remarks>
    void Start()
    {
        animator = GetComponent<Animator>();
    }

    /// <summary>
    /// Triggers the animator object 
    /// </summary>
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.P))
        {
            animator.SetTrigger("tutorial");
            animator.SetInteger("tut2", 1);
        }
    }
}
