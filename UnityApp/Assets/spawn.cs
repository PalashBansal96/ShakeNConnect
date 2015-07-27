using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class spawn : MonoBehaviour {

	GameObject[] card = new GameObject[5];
	public string[] id= new string[5];
	public GameObject c1;
	public Text dname, demail, dphone;
	string[] url = new string[3];

	// Use this for initialization
	void Start () {
		//PlayerPrefs.SetString ("id", "1");
		gameObject.GetComponent<Canvas>().enabled = false;
		card[0] = GameObject.Find ("Card");
		card[1] = GameObject.Find ("Card 1");
		card[2] = GameObject.Find ("Card 2");
		card[3] = GameObject.Find ("Card 3");
		card[4] = GameObject.Find ("Card 4");
		WWW www = new WWW ("http://192.168.2.26:8000/req/?id="+PlayerPrefs.GetString("id"));
		StartCoroutine (WaitForResponse (www));
	}

	IEnumerator WaitForResponse(WWW www){
		yield return www;
		if (www.error == null) {
			string response = System.Text.Encoding.UTF8.GetString (www.bytes);
			Debug.Log (response);
			char[] cc = {'|'};
			string[] vals = response.Split (cc);
			int no = int.Parse (vals [0]);
			for (int i=0; i<no; i++) {
				compo v = card [i].GetComponent<compo> ();
				v.id = vals [i * 4 + 1];
				id[i]=vals[i*4+1];
				Debug.Log (v.id);
				v.name.text = vals [i * 4 + 2];
				Debug.Log (v.name.text);
				v.time.text = vals [i * 4 + 3];
				Debug.Log (v.time.text);
				v.location.text = vals [i * 4 + 4];
				Debug.Log (v.location.text);
			}
			for(int i=no;i<5;i++){
				card[i].SetActive(false);
			}
			gameObject.GetComponent<Canvas>().enabled = true;
		} else {
			Debug.Log(www.error);
			gameObject.GetComponent<Canvas>().enabled = true;
		}
	}
	void reload(){
	
	}

	// Update is called once per frame
	void Update () {
		if (Input.GetKeyDown (KeyCode.A))
			Application.LoadLevel(Application.loadedLevel);
	}

	public void agree(int i){
		Debug.Log ("agree" + i);
		WWW www = new WWW ("http://192.168.2.26:8000/fin/?me="+PlayerPrefs.GetString("id")+"&you="+id[i]+"&s=1");
		StartCoroutine (WaitForRequest2(www));
	}

	public void reject(int i){
		Debug.Log ("rej" + i);
		WWW www = new WWW ("http://192.168.2.26:8000/fin/?me="+PlayerPrefs.GetString("id")+"&you="+id[i]+"&s=-1");
		Application.LoadLevel (Application.loadedLevelName);
	}

	IEnumerator WaitForRequest2(WWW www){
		yield return www;
		if (www.error == null) {
			string response = System.Text.Encoding.UTF8.GetString (www.bytes);
			Debug.Log (response);
			char[] cc = {'|'};
			string[] vals = response.Split (cc);
			//Debug.Log(GameObject.Find("DName"));
			dname.text=vals[0];
			demail.text=vals[1];
			dphone.text=vals[2];
			url[0] = vals[3];
			url[1] = vals[4];
			url[2] = vals[5];
			gameObject.GetComponent<Canvas>().enabled = false;
			c1.SetActive(true);
		} else
			Debug.Log (www.error);
	}

	public void goBack(){
		c1.SetActive(false);
		gameObject.GetComponent<Canvas>().enabled = true;
	}
	public void openURL(int i){
		Application.OpenURL (url [i]);
	}
}
