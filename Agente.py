import getSNMP as snmp
from Reporte import creandoReporte


class Agente():
    comunidad = ''
    ip = ''
    nombreAgente = ''
    sistemaOperativo = ''
    versionSO = ''
    contacto = ''
    ubicacion = ''
    numeroInterfaces = ''
    interfaces = {}
    estado = ''
    snmpVersion = ''
    puerto = ''

    def __init__(self):
        self.comunidad = ''
        self.ip = ''
        self.nombreAgente = ''
        self.sistemaOperativo = ''
        self.versionSO = ''
        self.contacto = ''
        self.ubicacion = ''
        self.numeroInterfaces = ''
        self.interfaces = {}
        self.estado = ''
        self.snmpVersion = ''
        self.puerto = ''

    def obtenerSO(self):
        aux = snmp.consultaSNMP(self.comunidad, self.ip, '1.3.6.1.2.1.1.1.0')
        if aux.find('#') != -1:
            if (aux.find("Ubuntu") > 0):  # En caso de ser Ubuntu
                soaux = aux.split()[5]
                ''.join(soaux)
                self.sistemaOperativo = soaux[soaux.find('-') + 1:]
        else:
            self.sistemaOperativo = aux.split()[14]
            self.versionSO = aux.split()[16]

    def obtenerUbicacion(self):
        aux = snmp.consultaSNMP(self.comunidad, self.ip, '1.3.6.1.2.1.1.6.0')
        aux = aux.split('=')
        self.ubicacion = aux[-1]

    def obtenerNombre(self):
        aux = snmp.consultaSNMP(self.comunidad, self.ip, '1.3.6.1.2.1.1.5.0')
        aux = aux.split('=')
        self.nombreAgente = aux[-1]


    def obtenerContacto(self):
        aux = snmp.consultaSNMP(self.comunidad, self.ip, '1.3.6.1.2.1.1.4.0')
        aux = aux.split('=')
        self.contacto = aux[-1]

    def obtenerInterfaces(self):
        aux = snmp.consultaSNMP(self.comunidad, self.ip, '1.3.6.1.2.1.2.1.0')
        aux = aux.split('=')
        self.numeroInterfaces = aux[-1]
        i = 1
        while (i <= int(self.numeroInterfaces)):
            aux = snmp.consultaSNMP(self.comunidad, self.ip, '1.3.6.1.2.1.2.2.1.8.' + str(i))
            aux = aux.split('=')
            self.interfaces[i] = aux[-1]
            i += 1
    """
    def obtenerEstados(self):
        self.numeroInterfaces = snmp.consultaSNMP(self.comunidad, self.ip, '1.3.6.1.2.1.2.1.0')
        intEst = []
        for i in range(1, int(self.numeroInterfaces).split('=')):
            aux = snmp.consultaSNMP(self.comunidad, self.ip, '1.3.6.1.2.1.2.2.1.8.' + str(i))
            intEst[i] = aux.split()[4]
            self.estado = intEst[i]
    """
    def crearReporte(self):
        self.obtenerSO()
        self.obtenerContacto()
        self.obtenerUbicacion()
        self.obtenerInterfaces()
        self.obtenerNombre()
        creandoReporte(self)
