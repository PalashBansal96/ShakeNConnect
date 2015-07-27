using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class RegisterScript : MonoBehaviour {

	public GameObject can1, can2;

	// Use this for initialization
	void Start () {
		//PlayerPrefs.DeleteAll();

		if (PlayerPrefs.HasKey("id")) {
			can2.SetActive (false);
			can1.SetActive (true);
		} else {
			can1.SetActive (false);
			can2.SetActive (true);
		}
	}
	
	// Update is called once per frame
	void Update () {
	
	}

	public void PerformRegister(){

		WWWForm form = new WWWForm();
		form.AddField("name",GameObject.Find("Name").GetComponent<InputField>().text);
		form.AddField("email", GameObject.Find("EMail").GetComponent<InputField>().text);
		form.AddField("number", GameObject.Find("Phone").GetComponent<InputField>().text);
		form.AddField("id", GameObject.Find("PIN").GetComponent<InputField>().text);
		form.AddField("git", GameObject.Find("git").GetComponent<InputField>().text);
		form.AddField("fb", GameObject.Find("fb").GetComponent<InputField>().text);
		form.AddField("link", GameObject.Find("link").GetComponent<InputField>().text);
		PlayerPrefs.SetString ("id", GameObject.Find ("PIN").GetComponent<InputField> ().text);
		Debug.Log (GameObject.Find("PIN").GetComponent<InputField>().text);
		WWW www = new WWW("http://192.168.2.26:8000/reg/", form);
		StartCoroutine(WaitForRequest (www));
	}	

	IEnumerator WaitForRequest(WWW www){
		yield return www;
		if (www.error == null) {
			Debug.Log (System.Text.Encoding.UTF8.GetString (www.bytes));
		} else
			Debug.Log (www.error);
		Application.LoadLevel(Application.loadedLevel);
	}

}
