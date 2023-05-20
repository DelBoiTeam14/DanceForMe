using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BotDance : MonoBehaviour
{
    Animator animator;
    int isJumpHash;
    int isTPoseHash;

    ///<summary>
    /// Setting the Animator game object to the animator class variable.
    ///</summary>
    void Start()
    {
        animator = GetComponent<Animator>();
        isJumpHash = Animator.StringToHash("isJump");
        isTPoseHash = Animator.StringToHash("isTPose");
    }

    ///<summary>
    /// Checks the animator's movements.
    ///</summary>
    void Update()
    {
        bool isJump = animator.GetBool(isJumpHash);
        bool jumpPress = Input.GetKey("w");
        bool isTpose = animator.GetBool(isTPoseHash);
        bool TPress = Input.GetKey("q");

        if (!isJump && jumpPress) {
            animator.SetBool(isJumpHash, true);
            Debug.Log("JUMP");
           
        }
        if (isJump && !jumpPress) {
            animator.SetBool(isJumpHash, false);
            Debug.Log("Back to Idle");
        }

        if (!isTpose && TPress)
        {
            animator.SetBool(isTPoseHash, true);
            Debug.Log("T Pose");

        }
        if (isTpose && !TPress)
        {
            animator.SetBool(isTPoseHash, false);
            Debug.Log("Back to Idle");
        }

    }
}
