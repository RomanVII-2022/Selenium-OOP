from booking.booking import Booking


with Booking(teardown=True) as bot:
    bot.land_page()
    #bot.change_currency("NOK")
    bot.place_to_go(input("Place you want to go? "))
    bot.check_in_and_check_out(input("Year and month check-in? "), input("day of check-in? "), input("Year and month check-out? "), input("day of check-out? "))
    bot.number_of_adults()
    bot.search_button()
    try:
        bot.pop_up()
    except:
        pass
    bot.apply_filtrations()
    bot.fiitration_information()