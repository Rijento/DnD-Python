class Feat(object):
    def __init__(self,name,desc):
        self.name = name
        self.desc = desc
    def getFeatName(self):
        return self.name
    def getFeatDesc(self):
        return self.desc

alert = Feat('Alert',
    '• You gain a +5 bonus to initiative.\n'+
    '• You can\'t be surprised while you are conscious.\n'+
    '• Other creatures don\'t gain advantage on attack rolls\n'+
    '   against you as a result of being hidden from you.'
    )
athlete = Feat('Athlete',
    '• When you are prone, standing up uses only 5 feet of\n'+
    '  your movement.\n'+
    '• Climbing doesn\'t halve your speed.\n'+
    '• You can make a running long jump or a running high\n'+
    '  jump after moving only 5 feet on foot, rather than\n'+
    '  10 feet.'
    )