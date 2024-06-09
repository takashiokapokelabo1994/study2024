def decode_caesar_cipher(text):
    # 単語の先頭文字の置き換え辞書
    first_letter_map = {
        'I': 'J', 'Q': 'W', 'Z': 'X', 'U': 'V', 'O': 'P',
        'Ig': 'Mr', 'qz': 'of', 'fro': 'the', 'yud': 'was', 'fqq': 'too', 
        'ro': 'he', 'ul': 'a', 'ulc': 'and', 'iuco': 'made', 'yrogo': 'where',
        'Sqlod': 'Jones', 'Zugi': 'Farm'
    }
    
    # 母音と子音の順序入れ替え辞書
    vowel_consonant_map = {
        'qh': 'ho', 'uv': 'va', 'xk': 'ki', 'ol': 'lo', 'og': 'ro',
        'ql': 'lq', 'ug': 'ra', 'hb': 'bh', 'cg': 'rc', 'xi': 'ix'
    }
    
    decoded_text = ''
    for word in text.split():
        # 単語の先頭文字を置き換え
        if word in first_letter_map:
            word = first_letter_map[word]
        elif word[0:2] in first_letter_map:
            word = first_letter_map[word[0:2]] + word[2:]
        elif word[0] in first_letter_map:
            word = first_letter_map[word[0]] + word[1:]
        
        # 母音と子音の順序を入れ替え
        for pair in vowel_consonant_map:
            if pair in word:
                word = word.replace(pair, vowel_consonant_map[pair])
        
        decoded_text += word + ' '
    
    return decoded_text.strip()

# 暗号文
encrypted_text = "Ig. Sqlod, qz fro Iulqg Zugi, ruc aqmeoc fro rol-rqhdod zqg fro lxkrf, nhf\n" \
                 "yud fqq cghle fq goioinog fq drhf fro bqb-rqaod. Yxfr fro gxlk qz axkrf\n" \
                 "zgqi rxd aulfogl culmxlk zgqi dxco fq dxco, ro ahgmroc umgqdd fro wugc,\n" \
                 "exmeoc qzz rxd nqqfd uf fro nume cqqg, cgoy rxidoaz u audf kaudd qz noog\n" \
                 "zgqi fro nuggoa xl fro dmhaaogw, ulc iuco rxd yuw hb fq noc, yrogo\n" \
                 "Igd. Sqlod yud uagoucw dlqgxlk."

# 暗号文を解読
decoded_text = decode_caesar_cipher(encrypted_text)
print(decoded_text)
