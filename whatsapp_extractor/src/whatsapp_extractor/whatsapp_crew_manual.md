# WhatsApp Crew Manual

## Overview
The WhatsApp Crew is a CrewAI-based implementation for extracting and analyzing WhatsApp chat data using Selenium. This tool connects to an existing WhatsApp Web session and provides automated data extraction capabilities.

## Prerequisites
- Python 3.8+
- Google Chrome browser
- WhatsApp Web access
- Required Python packages:
  ```bash
  pip install selenium crewai langchain
  ```

## Project Structure
```
whatsapp_extractor/
├── config/
│   ├── agents.yaml    # Agent configurations
│   └── tasks.yaml     # Task definitions
├── tools/
│   └── whatsapp_selenium_tool.py    # Selenium-based extraction tool
├── crew.py            # CrewAI implementation
└── main.py           # Entry point
```

## Components

### 1. Agents
The system uses two specialized agents:

#### WhatsApp Data Extraction Specialist
- Role: Extracts data from WhatsApp Web
- Tools: WhatsAppSeleniumTool
- Responsibilities:
  - Navigate WhatsApp Web interface
  - Extract chat lists and messages
  - Maintain data integrity

#### WhatsApp Data Processing Analyst
- Role: Processes extracted data
- Responsibilities:
  - Organize raw chat data
  - Identify patterns and insights
  - Generate structured reports

### 2. Tasks

#### Extract Chats Task
- Purpose: List all available chats
- Output: List of chat names and metadata
- Agent: Researcher (Extraction Specialist)

#### Extract Messages Task
- Purpose: Extract messages from specified chat
- Output: Timestamped messages with sender information
- Agent: Researcher (Extraction Specialist)

#### Process Data Task
- Purpose: Analyze and organize extracted data
- Output: JSON-formatted report with insights
- Agent: Data Processor

### 3. Selenium Tool
The WhatsAppSeleniumTool provides the following capabilities:
- Connect to existing Chrome session
- Extract chat lists
- Search and select specific chats
- Extract message history
- Handle timestamps and metadata

## Setup Instructions

### 1. Chrome Setup
1. Start Chrome with remote debugging enabled:
   ```bash
   google-chrome --remote-debugging-port=9222
   ```
2. Open WhatsApp Web (https://web.whatsapp.com)
3. Scan QR code to log in

### 2. Configuration
1. Update input parameters in main.py:
   ```python
   inputs = {
       'chat_name': 'Your Chat Name',  # Target chat to extract
       'max_messages': 100             # Maximum messages to extract
   }
   ```

### 3. Running the Tool
1. Execute the main script:
   ```bash
   python -m whatsapp_extractor.main
   ```
2. Results will be saved to `whatsapp_data.json`

## Usage Examples

### Basic Extraction
```python
from whatsapp_extractor.crew import WhatsappExtractor

# Configure extraction parameters
inputs = {
    'chat_name': 'Family Group',
    'max_messages': 100
}

# Run extraction
extractor = WhatsappExtractor()
results = extractor.crew().kickoff(inputs=inputs)
```

### Training Mode
```bash
python -m whatsapp_extractor.main train 5 training_data.json
```

### Replay Mode
```bash
python -m whatsapp_extractor.main replay task_123
```

## Security Considerations
- The tool requires an already authenticated WhatsApp Web session
- No credentials are stored or handled by the tool
- Data is processed locally and saved to local JSON files
- Chrome debugging port should only be enabled during tool usage

## Troubleshooting

### Common Issues
1. Chrome Connection Error
   - Ensure Chrome is running with --remote-debugging-port=9222
   - Check if WhatsApp Web is properly loaded

2. Extraction Failures
   - Verify WhatsApp Web session is active
   - Check chat name matches exactly
   - Ensure sufficient wait times for message loading

3. Data Processing Issues
   - Check JSON file permissions
   - Verify chat contains messages
   - Ensure proper encoding for special characters

### Debug Mode
Enable verbose logging in crew.py:
```python
@crew
def crew(self) -> Crew:
    return Crew(
        agents=self.agents,
        tasks=self.tasks,
        verbose=2,  # Set to 2 for detailed logging
        process=Process.sequential
    )
```

## Best Practices
1. Always use an active WhatsApp Web session
2. Start with small message limits for testing
3. Handle rate limiting and pagination
4. Regularly save extracted data
5. Validate chat names before extraction
6. Monitor Chrome debugging port security

## Contributing
1. Fork the repository
2. Create a feature branch
3. Implement changes
4. Add tests if applicable
5. Submit pull request

## License
This project is licensed under MIT License.

## Support
For issues and feature requests, please create an issue in the repository.
