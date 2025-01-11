text = input(
    "Введите текст который нужно закодировать при помощи алгоритм Хаффмана:\n\
(в шифровании не учитывается регистр символов)\n\
\n\
"
)


# все в нижний регистр
text = text.lower()
listed_text = list(text)


# просто список всех символов
symbols = list(set(listed_text))


# словарь с частотностью каждого символа
freq_repo = {}
for el in symbols:
    i = 1
    for beg_el in text:
        if el == beg_el:
            freq_repo[el] = i
            i += 1


# почему эта функция работала с sorted_direction?
# зачем вообще функция
# не суть, тут идет возрастающая сортировака символов по их частотности
def sorting(freq_repo: dict) -> list:
    """
    Функция сортирующая список элементов' по их частотности
    """
    sorted_direction = sorted(freq_repo.items(), key=lambda item: item[1])
    return sorted_direction


print("Частота букв в тексте: ", sorting(freq_repo))


# инициализация класса для узлов
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


# создание изначального списка с недоузлами
nodes = [Node(char, freq) for char, freq in freq_repo.items()]


# списковые вложения рулят
def huffman_encoding(nodes):
    # пока все не свяжется в один узел
    while len(nodes) > 1:
        # сортировка списка узлов по возрастанию веса
        nodes.sort(key=lambda x: x.freq)
        # берем те которые образуют минимальную сумму
        left = nodes.pop(0)
        right = nodes.pop(0)

        # инициализируем новый узел и конфигурируем его
        # Частота нового узла равна сумме частот его левого и правого подузлов
        new_node = Node(None, left.freq + right.freq)

        new_node.left = left
        new_node.right = right
        nodes.append(new_node)
    huffman_codes = {}

    def search(node, code=""):
        if node.char:
            huffman_codes[node.char] = code
            return
        search(node.left, code + "0")
        search(node.right, code + "1")

    root = nodes[0]
    search(root)

    return huffman_codes


codes = huffman_encoding(nodes)

print("Таблица кодов Хаффмана:")
for char, code in codes.items():
    print(f"{char}: {code}")


def encode_text(text, codes):
    encoded_text = " "
    # sep = '|'
    for char in text:
        encoded_text += codes[char]
        # encode_text += sep
    return encoded_text


encoded_text = encode_text(text, codes)
print("Закодированный текст:", encoded_text)
