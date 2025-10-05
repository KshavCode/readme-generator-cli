import { useState } from "react";
import { ScrollView, StyleSheet, Text, TextInput, TouchableOpacity, View } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";

function App() {
  const [name, setName] = useState("");
  const [desc, setDesc] = useState("");
  const [lang, setLang] = useState("");
  const [pack, setPack] = useState("");
  const [plans, setPlans] = useState("");
  const [installationGuide, setInstallationGuide] = useState("");

  const addField = () => {
    return (
      <View styles={{borderTopWidth: 1, borderColor: 'black', width: '100%'}}>
      <TextInput 
          multiline={true}
          placeholder="" 
          value={desc}
          onChangeText={setDesc} 
          style={styles.input}/>
      </View>
    )
  }

  async function submitBtn() {
    if (plans.length===0){
      plans = 'None'
    }
    let url = `http://192.168.29.125:8000/?title=${encodeURIComponent(name)}&description=${encodeURIComponent(desc)}&languages=${encodeURIComponent(lang)}&packages=${encodeURIComponent(pack)}&guide=${encodeURIComponent(installationGuide)}&plans=${encodeURIComponent(plans)}`;
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
      }

      const result = await response.json();
      alert(result);
    } catch (error) {
      alert(error.message);
    }
}
  return (
    <ScrollView>
      <SafeAreaView style={styles.container}>
        <Text style={styles.text}>GitHub README Creator</Text>
        <TextInput 
          maxLength={30}
          placeholder="Project Title" 
          value={name} 
          onChangeText={setName} 
          style={styles.input}/>
        <TextInput 
          multiline={true}
          placeholder="Project Description" 
          value={desc}
          onChangeText={setDesc} 
          style={styles.input}/>
        <TextInput 
          placeholder="Languages Used (e.g : Python, CSS, JS)" 
          value={lang}
          onChangeText={setLang} 
          style={styles.input}/>
        <TextInput 
          multiline={true}
          placeholder="Packages Used :
          (e.g : Angular, seperate with ; for languages and commas for multiple packages in one language)" 
          value={pack}
          onChangeText={setPack} 
          style={styles.input}/>
        <TextInput 
          multiline={true}
          numberOfLines={5}
          placeholder="Future Plans" 
          value={plans}
          onChangeText={setPlans} 
          style={styles.input}/>
        <TextInput 
          multiline={true}
          placeholder="Installation Guide" 
          value={installationGuide}
          onChangeText={setInstallationGuide} 
          style={styles.input}/>
        <View style={{width: '100%', alignItems: 'center', marginTop: 10}}>
          <TouchableOpacity 
            style={styles.button} 
            onPress={submitBtn}>
            <Text 
              style={styles.buttonText}>
              Save & Confirm
            </Text>
          </TouchableOpacity>
          <TouchableOpacity 
            style={[styles.button, {backgroundColor:"grey"}]} 
            disabled={true}>
            <Text 
              style={styles.buttonText}>
              Add Field (Coming Soon!)
            </Text>
          </TouchableOpacity>
        </View>
      </SafeAreaView>
    </ScrollView>
  );
}
export default App;

const styles = StyleSheet.create({
  container: {
    gap: 10,
    padding: 20,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  button: {
    marginTop: 10,
    paddingVertical: 10,
    paddingHorizontal: 20,
    borderRadius: 5,
    backgroundColor : 'black',
    width: '80%',
  },
  buttonText: {
    color: 'white',
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center'
  },
  text: {
    fontSize: 25,
    fontWeight: 'bold'
  },
  input: {
    fontSize: 18,
    borderWidth: 1,
    borderBottomWidth: 1,
    width: '100%',
    marginTop: 15,
    paddingHorizontal: 5,
    borderRadius: 5
  }
});