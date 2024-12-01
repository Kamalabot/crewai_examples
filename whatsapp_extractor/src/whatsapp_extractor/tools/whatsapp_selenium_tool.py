from typing import Type
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from langchain.tools import BaseTool
import time

class WhatsAppSeleniumTool(BaseTool):
    name = "WhatsApp Selenium Tool"
    description = "A tool to extract data from WhatsApp Web using Selenium"

    def __init__(self):
        super().__init__()
        self.driver = None

    def _run(self, command: str) -> str:
        """Execute the selenium command"""
        try:
            if not self.driver:
                # Attach to existing Chrome session
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                self.driver = webdriver.Chrome(options=chrome_options)

            if command == "extract_chats":
                return self._extract_chats()
            elif command == "extract_messages":
                return self._extract_messages()
            elif command.startswith("search_chat:"):
                chat_name = command.split(":")[1]
                return self._search_and_select_chat(chat_name)
            else:
                return "Invalid command. Available commands: extract_chats, extract_messages, search_chat:[chat_name]"

        except Exception as e:
            return f"Error executing command: {str(e)}"

    def _extract_chats(self) -> str:
        """Extract all available chats"""
        try:
            # Wait for chat list to be visible
            chat_list = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[role='listitem']"))
            )
            
            chats = []
            for chat in chat_list:
                try:
                    chat_name = chat.find_element(By.CSS_SELECTOR, "span[title]").get_attribute("title")
                    chats.append(chat_name)
                except:
                    continue
            
            return "\n".join(chats)
        except Exception as e:
            return f"Error extracting chats: {str(e)}"

    def _search_and_select_chat(self, chat_name: str) -> str:
        """Search and select a specific chat"""
        try:
            # Click search button
            search_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='textbox']"))
            )
            search_button.click()
            
            # Enter chat name
            search_button.send_keys(chat_name)
            time.sleep(2)  # Wait for search results
            
            # Click on the first result
            chat_result = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"span[title='{chat_name}']"))
            )
            chat_result.click()
            
            return f"Successfully opened chat: {chat_name}"
        except Exception as e:
            return f"Error searching chat: {str(e)}"

    def _extract_messages(self) -> str:
        """Extract messages from the current chat"""
        try:
            # Wait for messages to load
            message_list = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.message-in, div.message-out"))
            )
            
            messages = []
            for message in message_list:
                try:
                    text = message.find_element(By.CSS_SELECTOR, "span.selectable-text").text
                    time = message.find_element(By.CSS_SELECTOR, "span[data-pre-plain-text]").get_attribute("data-pre-plain-text")
                    messages.append(f"{time}: {text}")
                except:
                    continue
            
            return "\n".join(messages)
        except Exception as e:
            return f"Error extracting messages: {str(e)}"

    def _arun(self, query: str) -> str:
        """Async implementation"""
        raise NotImplementedError("WhatsAppSeleniumTool does not support async operations")
