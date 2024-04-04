try:
    from janome_handler import janome_handler 
except ImportError:
    from src.janome_handler import handler
handler = handler()

data = handler.analyze("文章を形態素解析した結果を返します。")

words = handler.split_sentence("文章を形態素解析によって分割したものを返します。")
