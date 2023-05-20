using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Diagnostics;
using System.ComponentModel;
using System.Threading;
using System.IO;
//FIXME: Should delete this when the project is done esting.
public class StartPython : MonoBehaviour
{
    static string mainPath;
    [SerializeField] public string PythonFileName;
    // Start is called before the first frame update
    void Start()
    {
        mainPath = Application.dataPath + "/Scripts/PythonScripts/";
        ExecuteCommand(PythonFileName);
    }

    // Update is called once per frame
    void Update()
    {
    }


    public static void ExecuteCommand(string directory)
    {
        var thread = new Thread(delegate () { Command(directory); });
        thread.Start();
    }

    static void Command(string input)
    {
        var processInfo = new ProcessStartInfo();
        //var process = new Process();
        processInfo.FileName = @"python.exe";
        processInfo.Arguments = input + ".py";
        //processInfo.WorkingDirectory = @"C:\Users\atris\Downloads\";
        //processInfo.Arguments = "PersonDetect.py";
        processInfo.WorkingDirectory = mainPath;
        processInfo.UseShellExecute = false;
        processInfo.RedirectStandardInput = true;
        processInfo.RedirectStandardOutput = true;
        var process = Process.Start(processInfo);

        while (!process.HasExited && !process.StandardOutput.EndOfStream)
        {
            // Read the output
            string output = process.StandardOutput.ReadLine();
            print(output);
        }
        //   var process = Process.Start(processInfo);

              process.WaitForExit();
             process.Close();
    }
}
