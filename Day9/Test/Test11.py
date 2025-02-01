#logger
class Warning:
    pass

class Error:
    pass

class Info:
    pass

warningobj = Warning()
errorobj = Error()
infoobj = Info()
class Logger:
    def log(self,message,warning:Warning):
        if warning:
            print("Warning: "+message)
        else:
            print(message)

    def log(self,message,error:Error):
        if error:
            print("Error: "+message)
        else:
            print(message)

    def log(self,message,info:Info):
        if info:
            print("Info: "+message)
        else:
            print(message)

obj = Logger()
obj.log("This is a log message",warningobj)
obj.log("This is a log message",errorobj)
obj.log("This is a log message",infoobj)