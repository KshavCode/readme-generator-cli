import React, { useState } from "react";
import {
  Platform,
  ScrollView,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";

function App() {
  const [name, setName] = useState("");
  const [desc, setDesc] = useState("");
  const [lang, setLang] = useState("");
  const [pack, setPack] = useState("");
  const [plans, setPlans] = useState("");
  const [installationGuide, setInstallationGuide] = useState("");
  const [fields, setFields] = useState([]);

  const addField = () => {
    const id = Date.now().toString();
    setFields((prev) => [
      ...prev,
      { id, label: `Custom Field ${prev.length + 1}`, value: "" },
    ]);
  };

  const updateField = (id, value) => {
    setFields((prev) => prev.map((f) => (f.id === id ? { ...f, value } : f)));
  };

  const removeField = (id) => {
    setFields((prev) => prev.filter((f) => f.id !== id));
  };

  async function submitBtn() {
    const plansValue = plans.length === 0 ? "None" : plans;
    const IP_ADD = require("../secret").IP_ADD;
    const custom = JSON.stringify(
      fields.map((f) => ({ label: f.label, value: f.value }))
    );

    const url = `http://${IP_ADD}:8000/generate?title=${encodeURIComponent(
      name
    )}&description=${encodeURIComponent(
      desc
    )}&languages=${encodeURIComponent(
      lang
    )}&packages=${encodeURIComponent(
      pack
    )}&guide=${encodeURIComponent(
      installationGuide
    )}&plans=${encodeURIComponent(plansValue)}&custom=${encodeURIComponent(
      custom
    )}`;

    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
      }
      const result = await response.json();
      if (result && result.message) {
        alert(result.message);
      } else if (result && result.success) {
        alert("Success: " + (result.title || "README saved"));
      } else if (result && result.error) {
        alert("Error: " + result.error);
      } else {
        alert(JSON.stringify(result));
      }
    } catch (error) {
      alert(error.message);
    }
  }

  return (
    <ScrollView contentContainerStyle={styles.scroll}>
      <SafeAreaView style={styles.container}>
        <Text style={styles.header}>GitHub README Creator</Text>

        <View style={styles.card}>
          <Text style={styles.label}>Project Title</Text>
          <TextInput
            maxLength={50}
            placeholder="e.g. My Cool App"
            value={name}
            onChangeText={setName}
            style={styles.input}
            placeholderTextColor="#888"
          />

          <Text style={styles.label}>Project Description</Text>
          <TextInput
            multiline
            placeholder="A short description of the project"
            value={desc}
            onChangeText={setDesc}
            style={[styles.input, styles.textArea]}
            placeholderTextColor="#888"
          />

          <Text style={styles.label}>Languages Used</Text>
          <TextInput
            placeholder="e.g. Python, CSS, JS"
            value={lang}
            onChangeText={setLang}
            style={styles.input}
            placeholderTextColor="#888"
          />

          <Text style={styles.label}>Packages / Frameworks</Text>
          <TextInput
            multiline
            placeholder="e.g. React; Angular (separate languages with ;) or packages with commas"
            value={pack}
            onChangeText={setPack}
            style={[styles.input, styles.textArea]}
            placeholderTextColor="#888"
          />

          <Text style={styles.label}>Future Plans</Text>
          <TextInput
            multiline
            numberOfLines={4}
            placeholder="Future improvements or roadmap"
            value={plans}
            onChangeText={setPlans}
            style={[styles.input, styles.textArea]}
            placeholderTextColor="#888"
          />

          <Text style={styles.label}>Installation Guide</Text>
          <TextInput
            multiline
            placeholder="Steps to install and run the project"
            value={installationGuide}
            onChangeText={setInstallationGuide}
            style={[styles.input, styles.textArea]}
            placeholderTextColor="#888"
          />
        </View>

        <View style={[styles.card, styles.customCard]}>
          <View style={styles.customHeader}>
            <Text style={styles.label}>Custom Fields</Text>
            <TouchableOpacity style={styles.addButton} onPress={addField}>
              <Text style={styles.addButtonText}>+ Add Field</Text>
            </TouchableOpacity>
          </View>

          {fields.length === 0 ? (
            <Text style={styles.hint}>No custom fields yet — add one.</Text>
          ) : (
            fields.map((f) => (
              <View key={f.id} style={styles.fieldRow}>
                <View style={{ flex: 1 }}>
                  <Text style={styles.smallLabel}>{f.label}</Text>
                  <TextInput
                    placeholder="Field value"
                    value={f.value}
                    onChangeText={(v) => updateField(f.id, v)}
                    style={styles.input}
                    placeholderTextColor="#888"
                  />
                </View>

                <TouchableOpacity
                  style={styles.removeButton}
                  onPress={() => removeField(f.id)}
                >
                  <Text style={styles.removeButtonText}>Remove</Text>
                </TouchableOpacity>
              </View>
            ))
          )}
        </View>

        <View style={styles.actions}>
          <TouchableOpacity style={styles.primaryButton} onPress={submitBtn}>
            <Text style={styles.primaryButtonText}>Save & Confirm</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.secondaryButton]}
            onPress={() => {
              // quick clear for demo convenience
              setName("");
              setDesc("");
              setLang("");
              setPack("");
              setPlans("");
              setInstallationGuide("");
              setFields([]);
            }}
          >
            <Text style={styles.secondaryButtonText}>Reset</Text>
          </TouchableOpacity>
        </View>
      </SafeAreaView>
    </ScrollView>
  );
}

export default App;

const styles = StyleSheet.create({
  scroll: {
    flexGrow: 1,
    backgroundColor: "#f3f6fb",
    paddingVertical: Platform.OS === "android" ? 20 : 40,
  },
  container: {
    paddingHorizontal: 20,
    alignItems: "stretch",
  },
  header: {
    fontSize: 26,
    fontWeight: "800",
    color: "#0b3d91",
    marginBottom: 16,
    textAlign: "center",
  },
  card: {
    backgroundColor: "#ffffff",
    borderRadius: 12,
    padding: 14,
    marginBottom: 14,
    // iOS shadow
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.08,
    shadowRadius: 10,
    // Android elevation
    elevation: 3,
  },
  customCard: {
    paddingBottom: 10,
  },
  label: {
    fontSize: 16,
    fontWeight: "700",
    color: "#213547",
    marginBottom: 6,
    marginTop: 10,
  },
  smallLabel: {
    fontSize: 12,
    fontWeight: "600",
    color: "#213547",
    marginBottom: 4,
  },
  input: {
    fontSize: 15,
    backgroundColor: "#f9fbff",
    borderWidth: 1,
    borderColor: "#e6eefc",
    paddingHorizontal: 10,
    paddingVertical: 8,
    borderRadius: 8,
    color: "#123",
  },
  textArea: {
    minHeight: 80,
    textAlignVertical: "top",
    marginTop: 6,
  },
  actions: {
    marginTop: 8,
    marginBottom: 40,
    alignItems: "center",
  },
  primaryButton: {
    backgroundColor: "#0b3d91",
    paddingVertical: 12,
    paddingHorizontal: 28,
    borderRadius: 10,
    width: "85%",
    alignItems: "center",
    marginBottom: 10,
  },
  primaryButtonText: {
    color: "#fff",
    fontWeight: "700",
    fontSize: 16,
  },
  secondaryButton: {
    backgroundColor: "#e6eefc",
    paddingVertical: 10,
    paddingHorizontal: 20,
    borderRadius: 8,
    width: "85%",
    alignItems: "center",
  },
  secondaryButtonText: {
    color: "#0b3d91",
    fontWeight: "700",
    fontSize: 14,
  },
  addButton: {
    backgroundColor: "#0b84ff",
    paddingVertical: 6,
    paddingHorizontal: 10,
    borderRadius: 8,
  },
  addButtonText: {
    color: "#fff",
    fontWeight: "700",
  },
  removeButton: {
    marginLeft: 10,
    alignSelf: "flex-end",
    backgroundColor: "#ffdede",
    paddingVertical: 6,
    paddingHorizontal: 8,
    borderRadius: 8,
  },
  removeButtonText: {
    color: "#a10b0b",
    fontWeight: "700",
    fontSize: 12,
  },
  hint: {
    color: "#6b6f76",
    fontStyle: "italic",
  },
  customHeader: {
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: 8,
  },
  fieldRow: {
    flexDirection: "row",
    alignItems: "flex-start",
    marginBottom: 10,
  },
});