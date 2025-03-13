# **Logical Fallacy Recognition**  

A real-time analytical engine for uncovering logical inconsistencies in live debates and multimedia content. This project identifies flawed reasoning that may appear valid but are based on incorrect premises, making them difficult to catch in the heat of the moment.  

Currently, the system includes **speech-to-text recognition**, which captures audio from a microphone and converts it into text. The text is then analyzed using the **Gemini API** to detect logical fallacies. Future versions will improve accuracy and introduce more sophisticated analysis.  

## **Features**  

- **Speech-to-Text**: Converts live audio into text using Google's Speech Recognition API.  
- **Logical Fallacy Detection**: Processes text through the **Gemini API** to detect inconsistencies and flawed reasoning.  
- **Multi-Source Input Processing**: Supports debates, meetings, and social media content.  
- **Flask-Based Web Interface**: Enables real-time, multi-user fallacy detection with applications in **debate competitions, courtrooms, and news analysis**.  

## **Requirements**  

- Python 3.12+  
- Flask (for serving the application)  
- Google Speech-to-Text API  
- Gemini API (for fallacy detection)  
- YouTube-dlp, ffmpeg, pyaudio (for multimedia  processing)  

## **Setup Instructions**  

### **1. Clone the Repository**  

```bash
git clone https://github.com/Priyanshu-Builds/Logical_Fallacy_Recognition.git
cd logical_fallacy_recognition
```  

### **2. Install Dependencies**  

Use `pip` to install the necessary libraries listed in `requirements.txt`.  

```bash
pip install -r requirements.txt
```  

### **3. Add Your Gemini API Key**  

Create a `.env` file in the root directory and add your **Gemini API** key.  

```bash
GEMINI_API_KEY=your_gemini_api_key_here
```  

### **4. Run the Application**  

Start the Flask server:  

```bash
python server.py
```  

The application should now be running at `http://localhost:5000/`.  

## **Usage**  

1. **Live Speech Analysis**: Speak into the microphone. The system will capture your voice, convert it into text, and save it as `output.txt`.  
2. **Logical Analysis**: The text is processed using the **Gemini API** to detect any logical fallacies. Results are displayed on the web interface.  

## **Future Improvements**  

- Enhance fallacy detection with advanced AI models.  
- Improve accuracy and processing speed.  
- Expand dataset coverage for more robust logical analysis.  
- Implement real-time analysis from multiple sources (news, debates, podcasts).  

## **License**  

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.  
