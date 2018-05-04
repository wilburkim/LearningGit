def CalMoney(perSonCount, ballMoney, siteFee, siteFeeFreeCount, moneyLeft = 0):
    totalMoney = ballMoney + siteFee;
    feeEachPerson = totalMoney/perSonCount;
    print("场地费：",siteFee,"球费：",ballMoney,"每个人：", feeEachPerson);

    siteFeePerPerson = siteFee/perSonCount;

    ballMoneyPerPerson = ballMoney/perSonCount;

    inCome = (perSonCount - siteFeeFreeCount) * siteFeePerPerson;

    unCountBallMoney = siteFeeFreeCount* ballMoneyPerPerson;

    leftMoney = moneyLeft + inCome - unCountBallMoney;
    if(leftMoney >= 0):
        print("所收场地费充足，不需要额外缴费，剩余费用：",leftMoney)
    else:
        print("所收场地费不足以补充球费,每人需额外补充费用",leftMoney * -1 /siteFeeFreeCount);

CalMoney(11,73.7,215,5,0);

