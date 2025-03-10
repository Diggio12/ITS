soglia:int = 70
nord_sud:int = int(input('Inserire veicoli provenienti da direzione Nord Sud: '))
est_ovest:int = int(input('Inserire veicoli provenienti da direzione Est Ovest: '))
tempo_ns = 0
tempo_eo = 0

if nord_sud > soglia and est_ovest > soglia:
    tempo_ns = 50
    tempo_eo = 50
    print(f'Il tempo per la direzione Nord Sud sarà di: {tempo_ns}%, mentre il tempo per la direzione Est Ovest sarà di: {tempo_eo}%')
elif nord_sud > soglia and est_ovest < soglia:
    tempo_ns = 60
    tempo_eo = 40
    print(f'Il tempo per la direzione Nord Sud sarà di: {tempo_ns}%, mentre il tempo per la direzione Est Ovest sarà di: {tempo_eo}%')
elif nord_sud < soglia and est_ovest > soglia:
    tempo_ns = 40
    tempo_eo = 60
    print(f'Il tempo per la direzione Nord Sud sarà di: {tempo_ns}%, mentre il tempo per la direzione Est Ovest sarà di: {tempo_eo}%')
else:
    tempo_ns = (nord_sud / (nord_sud + est_ovest))*100
    tempo_eo = (est_ovest / (est_ovest + nord_sud))*100
    print(f'Il tempo per la direzione Nord Sud sarà di: {(tempo_ns):.1f}%, mentre il tempo per la direzione Est Ovest sarà di: {(tempo_eo):.1f}%')
