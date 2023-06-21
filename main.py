def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """

    males = int(input('Enter the number of male students: '))
    females = int(input('Enter the number of female students: '))
    total = males + females
    m_perc = 100 * (males / total)
    f_perc = 100 * (females / total)
    
    print(f'The total number of students:   \t {total}')
    print(f'The number of males and females \t {males}          \t {females}')
    print(f'The percentage of males and females \t {m_perc:.2f}% \t {f_perc:.2f}%')
    


    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
