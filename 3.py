class TextFileReader:
    def __init__(self, filename: str):
        self.filename = filename

    def read_all(self) -> str:
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                content = f.read()
            return content
        except FileNotFoundError:
            return f"Помилка: Файл '{self.filename}' не знайдено."
        except Exception as e:
            return f"Помилка читання файлу: {e}"

    def read_lines(self) -> list[str]:
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            return lines
        except FileNotFoundError:
            return [f"Помилка: Файл '{self.filename}' не знайдено."]
        except Exception as e:
            return [f"Помилка читання файлу: {e}"]

class TextFileWriter:
    def __init__(self, filename: str):
        self.filename = filename

    def write_content(self, content: str, mode: str = 'w') -> bool:
        if mode not in ['w', 'a']:
            print(f"Помилка: Невірний режим запису '{mode}'. Використовуйте 'w' або 'a'.")
            return False
            
        try:
            with open(self.filename, mode, encoding='utf-8') as f:
                f.write(content)
            print(f"Успішний запис у файл '{self.filename}' (режим: {mode}).")
            return True
        except Exception as e:
            print(f"Помилка запису файлу: {e}")
            return False

if __name__ == '__main__':
    target_file = "demo_data.txt"

    writer = TextFileWriter(target_file)
    writer.write_content("Рядок 1: Привіт.\nРядок 2: Команди.\n", mode='w')
    writer.write_content("Рядок 3: Додавання.\n", mode='a')

    reader = TextFileReader(target_file)
    full_content = reader.read_all()
    print("Повний вміст:")
    print(full_content)

    lines_list = reader.read_lines()
    print("Зчитані рядки:")
    for line in lines_list:
        print(line.strip())
