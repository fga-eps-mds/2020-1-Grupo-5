from src.bot import Bot

def main():

    try:
        bot = Bot()
        bot.run()
    
    except:
        
        print("\nAplicação finalizada")



if __name__ == '__main__':
    main()

