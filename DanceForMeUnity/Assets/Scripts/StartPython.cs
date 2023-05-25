using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Diagnostics;
using System.ComponentModel;
using System.Threading;
using System.IO;
/// <summary>
/// Class <c>StartPython</c> is used to test out python scripts without building executable every time
/// </summary>
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

    /// <summary>
    /// This method is used to call the python script specified by the Unity Editor. It will start a process using
    /// window command prompt 
    /// </summary>
    /// <param name="input">The file name of the python script</param>
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
