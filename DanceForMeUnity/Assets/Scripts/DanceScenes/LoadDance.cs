using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LoadDance : MonoBehaviour
{
    public Animator animator;
    public string choregraphy;
    public string modelName;
    // Start is called before the first frame update
    void Start()
    {
        animator = GetComponent<Animator>();
        if (modelName == "dellboi")
        {
            StartCoroutine(loadDance());
        }
        else
        {
            loadDance2();
        }
    }

    // Update is called once per frame
    void Update()
    {

    }



    public IEnumerator loadDance() {
        yield return new WaitForSeconds(3);
        animator.Play("#KinetixStack", -1, 0f);

    }

    public void loadDance2() {
        animator.Play("#KinetixStack", -1, 0f);
    }
}
