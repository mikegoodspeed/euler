singles = {'0': '', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
teens = {'0': 'ten', '1':'eleven', '2':'twelve', '3':'thirteen', '4':'fourteen', '5':'fifteen', '6':'sixteen', '7':'seventeen', '8':'eighteen', '9':'nineteen'}
tens = {'0': '', '1':'ten', '2':'twenty', '3':'thirty', '4':'forty', '5':'fifty', '6':'sixty', '7':'seventy', '8':'eighty', '9':'ninety'}

def wordlen(num):
    global singles
    global teens
    global tens
    if num == 1000:
        return 'onethousand'
    num = str(num)
    count = ''
    if len(num) == 1:
        count += singles[num]
    elif len(num) == 2:
        if num[0] == '1':
            count += teens[num[1]]
        else:
            count += tens[num[0]] + singles[num[1]]
    else:
        count += singles[num[0]] + 'hundred'
        if num[1:] != '00':
            count += 'and'
        if num[1] == '1':
            count += teens[num[2]]
        else:
            count += tens[num[1]] + singles[num[2]]
    return count

print sum(map(len, map(wordlen, range(1, 1001))))
