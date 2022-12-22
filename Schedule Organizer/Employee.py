class Employee:

    def __init__(self, name: str, shift: str):
        self.name = name
        self.shift = shift

        dots_entry = self.shift.find(':')
        entry_hour = self.shift[:dots_entry]
        entry_mins = self.shift[dots_entry+1:dots_entry+3]

        dots_out = self.shift.find(':', dots_entry+1)
        out_hour = self.shift[dots_out-2:dots_out] if not self.shift[dots_out-2:dots_out].startswith('-') else self.shift[dots_out-1:dots_out]
        out_mins = self.shift[dots_out+1:dots_out+3]
        
        self.shift_entry = float(str(entry_hour + '.' + entry_mins))
        self.shift_out = float(str(out_hour + '.' + out_mins))

        calcBreak = int(entry_hour) + 3
        self.Break = str(calcBreak) + ':' + entry_mins if calcBreak < 12 else str(calcBreak - 12) + ':' + entry_mins


        self.str_entry = entry_hour + ':' + entry_mins
        self.str_out = out_hour + ':' + out_mins

        '''
        Remember:
            Hay turnos con salida a la misma hora
            Hay turnos de ej 8:15 - 4:45
            Hay turnos de 4 horas que no tienen break


        if out = 5:00 cuadre = 4:30
        if out = 4:30 cuadre = 4:00

        '''

        