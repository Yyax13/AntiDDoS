class c:
    @staticmethod
    def black(text):
        return f"\033[0;30m{text}\033[0m"
    
    @staticmethod
    def red(text):
        return f"\033[0;31m{text}\033[0m"
    
    @staticmethod
    def green(text):
        return f"\033[0;32m{text}\033[0m"
    
    @staticmethod
    def brown(text):
        return f"\033[0;33m{text}\033[0m"
    
    @staticmethod
    def blue(text):
        return f"\033[0;34m{text}\033[0m"
    
    @staticmethod
    def purple(text):
        return f"\033[0;35m{text}\033[0m"
    
    @staticmethod
    def cyan(text):
        return f"\033[0;36m{text}\033[0m"
    
    @staticmethod
    def gray(text):
        return f"\033[1;30m{text}\033[0m"
    
    @staticmethod
    def yellow(text):
        return f"\033[1;33m{text}\033[0m"