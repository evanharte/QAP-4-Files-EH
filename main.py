# Program description: This is a program to help the One-Stop Insurance Company calculate new insurance policy
# information for its customers

# Import libraries
import FormatValues as FV
import time
from tqdm import tqdm
import datetime as dt
CurrDate = dt.datetime.now()
CurrDateF = dt.datetime.strftime(CurrDate, "%Y-%m-%d")


# Read values from OSICDef.dat file
f = open("OSICDef.dat", "r")
NextPolicyNum = int(f.readline())             # 1944
BasicPremium = float(f.readline())            # 869.00
AddCarDiscRate = float(f.readline())          # .25
ExtraLiabilityRate = float(f.readline())      # 130.00
GlassCoverageRate = float(f.readline())       # 86.00
LoanCarRate = float(f.readline())             # 58.00
HSTRate = float(f.readline())                 # .15
MonthlyPayFee = float(f.readline())           # 39.99
f.close()

# Main program / inputs / validations
ProvLst = ["AB", "BC", "MB", "NB", "NL", "NT", "NS", "NU", "ON", "PE", "QC", "SK", "YK"]
PayOptionLst = ["Full", "Monthly"]
YesNoLst = ["Y", "N"]

while True:
    print()

    while True:
        CustFName = input("Enter the customer first name: ").title()
        if CustFName == "":
            print("Error - Customer first name cannot be blank.")
        else:
            break

    while True:
        CustLName = input("Enter the customer last name: ").title()
        if CustLName == "":
            print("Error - Customer last name cannot be blank.")
        else:
            break

    while True:
        StAdd = input("Enter the street address: ").title()
        if StAdd == "":
            print("Error - The street address cannot be blank.")
        else:
            break

    while True:
        City = input("Enter the city: ").title()
        if City == "":
            print("Error - The city cannot be blank.")
        else:
            break

    while True:
        Prov = input("Enter the province ('AB', 'NL', 'ON' ...): ").upper()
        if Prov not in ProvLst:
            print("Error - Not a valid province OR invalid format. Please try again")
        else:
            break

    while True:
        PostCode = input("Enter the postal code (A1A1A1): ").upper()
        if PostCode == "":
            print("Error - Postal code cannot be blank.")
        elif not PostCode[0].isalpha():
            print("Error - The first character must be a letter.")
        elif not PostCode[1].isdigit():
            print("Error - The second character must be a number.")
        elif not PostCode[2].isalpha():
            print("Error - The third character must be a letter.")
        elif not PostCode[3].isdigit():
            print("Error - The fourth character must be a number.")
        elif not PostCode[4].isalpha():
            print("Error - The fifth character must be a letter.")
        elif not PostCode[5].isdigit():
            print("Error - The last character must be a number.")
        elif len(PostCode) != 6:
            print("Error - The postal code must be 6 characters (A1A1A1).")
        else:
            break

    while True:
        PhNum = input("Enter the phone number (###-###-####): ")
        if PhNum == "":
            print("Error - The phone number cannot be blank.")
        elif len(PhNum) != 12:
            print("Error - Invalid format. Please re-enter (###-###-####).")
        elif not PhNum[0:3].isdigit():
            print("Error - Invalid format. Please re-enter (###-###-####).")
        elif PhNum[3] != "-":
            print("Error - Invalid format. Please re-enter (###-###-####).")
        elif not PhNum[4:7].isdigit():
            print("Error - Invalid format. Please re-enter (###-###-####).")
        elif PhNum[7] != "-":
            print("Error - Invalid format. Please re-enter (###-###-####).")
        elif not PhNum[8:].isdigit():
            print("Error - Invalid format. Please re-enter (###-###-####).")
        else:
            break

    while True:
        try:
            NumCars = int(input("Enter the number of cars being insured: "))
        except:
            print("Error - Must be an integer. Please re-enter.")
        else:
            break

    while True:
        ExtraLiability = input("Would you like extra liability up to $1,000,000? (Y/N): ").upper()
        if ExtraLiability not in YesNoLst:
            print("Error - Please enter either 'Y' or 'N'.")
        else:
            break

    while True:
        GlassCoverage = input("Would you like glass coverage? (Y/N): ").upper()
        if GlassCoverage not in YesNoLst:
            print("Error - Please enter either 'Y' or 'N'.")
        else:
            break

    while True:
        LoanerCar = input("Would you like a loaner car? (Y/N): ").upper()
        if LoanerCar not in YesNoLst:
            print("Error - Please enter either 'Y' or 'N'.")
        else:
            break

    while True:
        PayOption = input("Would you like to pay in full or monthly? (Enter 'Full' or 'Monthly'): ").title()
        if PayOption not in PayOptionLst:
            print("Error - Pay option must be either 'Full' or 'Monthly'. Please re-enter.")
        else:
            break

    # Calculations
    if NumCars > 1:
        InsurancePrem = BasicPremium + ((BasicPremium * AddCarDiscRate) * (NumCars - 1))
    else:
        InsurancePrem = BasicPremium

    if ExtraLiability == "Y":
        ExtraLiabilityCost = ExtraLiabilityRate * NumCars
    else:
        ExtraLiabilityCost = 0

    if GlassCoverage == "Y":
        GlassCoverageCost = GlassCoverageRate * NumCars
    else:
        GlassCoverageCost = 0

    if LoanerCar == "Y":
        LoanerCarCost = LoanCarRate * NumCars
    else:
        LoanerCarCost = 0

    TotExtraCosts = ExtraLiabilityCost + GlassCoverageCost + LoanerCarCost
    TotInsurancePrem = InsurancePrem + TotExtraCosts
    HST = TotInsurancePrem * HSTRate
    TotCost = TotInsurancePrem + HST
    if PayOption == "Monthly":
        MonthlyPay = (TotCost + MonthlyPayFee) / 8
    else:
        MonthlyPay = 0

    InvDate = CurrDate

    if InvDate.month == 12:
        NextMonth = 1
        NextYear = InvDate.year + 1
    else:
        NextMonth = InvDate.month + 1
        NextYear = InvDate.year

    NextPayDate = dt.date(NextYear, NextMonth, 1)

    # Display receipt
    print()
    print("             ONE STOP INSURANCE COMPANY")
    print("                  CUSTOMER RECEIPT")
    print("   *********************************************")
    print()
    print(f"     Date: {CurrDateF}")
    print(f"     {CustLName}, {CustFName}")
    print(f"     {StAdd:<20s}, {City:<10s}, {Prov:<2s}")
    print(f"     {PostCode:<6s}, {PhNum:<12s}")
    print(f"     Policy #: {NextPolicyNum}")
    print("   =============================================")
    print()
    print(f"     No. of cars insured:             {NumCars}")
    if ExtraLiability == "Y":
        ExtraLiabilityF = "Yes"
    else:
        ExtraLiabilityF = "No"
    print(f"     Extra Liability:                 {ExtraLiabilityF}")
    if GlassCoverage == "Y":
        GlassCoverageF = "Yes"
    else:
        GlassCoverageF = "No"
    print(f"     Glass Coverage:                  {GlassCoverageF}")
    if LoanerCar == "Y":
        LoanerCarF = "Yes"
    else:
        LoanerCarF = "No"
    print(f"     Loaner Car:                      {LoanerCarF}")
    print(f"     Payment option:                  {PayOption}")
    print("   =============================================")
    print()
    print(f"     Insurance premium cost:        {FV.FDollar2(InsurancePrem):>9s}")
    if ExtraLiability == "Y":
        print(f"     Extra liability cost:          {FV.FDollar2(ExtraLiabilityCost):>9s}")
    if GlassCoverage == "Y":
        print(f"     Glass Coverage cost:           {FV.FDollar2(GlassCoverageCost):>9s}")
    if LoanerCar == "Y":
        print(f"     Loaner car cost:               {FV.FDollar2(LoanerCarCost):>9s}")
    print(f"     Total extra costs:             {FV.FDollar2(TotExtraCosts):>9s}")
    print(f"     Total insurance premium:       {FV.FDollar2(TotInsurancePrem):>9s}")
    print(f"     HST:                           {FV.FDollar2(HST):>9s}")
    print(f"     Total Cost:                    {FV.FDollar2(TotCost):>9s}")
    if PayOption == "Monthly":
        print(f"     Monthly Pay:                   {FV.FDollar2(MonthlyPay):>9s}")
    print(f"     Date of next payment:         {NextPayDate}")
    print("   =============================================")
    print()

    for _ in tqdm(range(20), desc="Processing", unit="ticks", ncols=100, bar_format="{desc}  {bar}"):
        time.sleep(.1)

    InvDateF = CurrDateF
    # Save policy number, all input values and the total insurance premium to Policies.dat
    f = open("Policies.dat", "a")
    f.write(f"{str(NextPolicyNum)}, ")
    f.write(f"{str(InvDateF)}, ")
    f.write(f"{CustFName}, ")
    f.write(f"{CustLName}, ")
    f.write(f"{StAdd}, ")
    f.write(f"{City}, ")
    f.write(f"{Prov}, ")
    f.write(f"{PostCode}, ")
    f.write(f"{PhNum}, ")
    f.write(f"{str(NumCars)}, ")
    f.write(f"{str(ExtraLiability)}, ")
    f.write(f"{str(GlassCoverage)}, ")
    f.write(f"{str(LoanerCar)}, ")
    f.write(f"{PayOption}, ")
    f.write(f"{TotInsurancePrem:.2f}\n")
    f.close()

    time.sleep(1)
    print()
    print("Policy information processed and saved ...")
    print()

    # Update Next policy number
    NextPolicyNum += 1

    Continue = input("Would you like to enter another policy? (Y/N): ").upper()
    if Continue == "N":
        break

f = open("OSICDef.dat", "w")
f.write(f"{str(NextPolicyNum)}\n")
f.write(f"{str(BasicPremium)}\n")
f.write(f"{str(AddCarDiscRate)}\n")
f.write(f"{str(ExtraLiabilityRate)}\n")
f.write(f"{str(GlassCoverageRate)}\n")
f.write(f"{str(LoanCarRate)}\n")
f.write(f"{str(HSTRate)}\n")
f.write(f"{str(MonthlyPayFee)}\n")
f.close()
