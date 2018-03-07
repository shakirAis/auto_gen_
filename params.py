"""
There are all parameters from perfect device (without services
and vendor specific parameters) which we have to show on the
Support Portal
"""


device_info = ["InternetGatewayDevice.DeviceInfo.ModelName", "InternetGatewayDevice.DeviceInfo.Manufacturer",
               "InternetGatewayDevice.DeviceInfo.ProductClass", "InternetGatewayDevice.DeviceInfo.UpTime",
               "InternetGatewayDevice.DeviceInfo.HardwareVersion", "InternetGatewayDevice.DeviceInfo.SoftwareVersion",
               "InternetGatewayDevice.DeviceInfo.SerialNumber"]

device_info_props = ["cpe.ip", "cpe.cpeid", "cpe.roles", "cpe.firstMsg", "cpe.lastMsg", "cpe.path"]

full_device_info = ["InternetGatewayDevice.DeviceInfo.Description",
                    "InternetGatewayDevice.DeviceInfo.Manufacturer",
                    "InternetGatewayDevice.DeviceInfo.ModelName",
                    "InternetGatewayDevice.DeviceInfo.SerialNumber",
                    "InternetGatewayDevice.DeviceInfo.HardwareVersion",
                    "InternetGatewayDevice.DeviceInfo.ModemFirmwareVersion",
                    "InternetGatewayDevice.DeviceInfo.SoftwareVersion",
                    "InternetGatewayDevice.DeviceInfo.ProductClass",
                    "InternetGatewayDevice.DeviceInfo.UpTime",
                    "InternetGatewayDevice.ManagementServer.EnableCWMP",
                    "InternetGatewayDevice.ManagementServer.PeriodicInformEnable",
                    "InternetGatewayDevice.ManagementServer.UpgradesManaged",
                    "InternetGatewayDevice.ManagementServer.ManageableDevice.1.ManufacturerOUI",
                    "InternetGatewayDevice.ManagementServer.ManageableDevice.1.Host",
                    "InternetGatewayDevice.ManagementServer.ConnectionRequestUsername",
                    "InternetGatewayDevice.ManagementServer.ConnectionRequestURL",
                    "InternetGatewayDevice.ManagementServer.PeriodicInformEnable",
                    "InternetGatewayDevice.ManagementServer.PeriodicInformTime",
                    "InternetGatewayDevice.ManagementServer.URL",
                    "InternetGatewayDevice.ManagementServer.UDPConnectionRequestAddress",
                    "InternetGatewayDevice.ManagementServer.STUNServerAddress",
                    "InternetGatewayDevice.ManagementServer.STUNEnable"]

time = ["InternetGatewayDevice.Time.Enable", "InternetGatewayDevice.Time.LocalTimeZone",
        "InternetGatewayDevice.Time.CurrentLocalTime",
        "InternetGatewayDevice.Time.Status", "InternetGatewayDevice.Time.NTPServer1",
        "InternetGatewayDevice.Time.NTPServer2",
        "InternetGatewayDevice.Time.NTPServer3", "InternetGatewayDevice.Time.NTPServer4",
        "InternetGatewayDevice.Time.NTPServer5"]

wan_ip = ["InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.Name",
          "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.Status",
          "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.ConnectionType",
          "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.AddressingType",
          "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.ExternalIPAddress",
          "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.SubnetMask",
          "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.DNSEnabled",
          "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.DNSServers",
          "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.Enable",
          "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.LastConnectionError",
          "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.MACAddress",
          "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.ConnectionStatus",
          "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.NATEnabled",
          "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.Uptime"
          ]

wan_ppp = ["InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.Name",
           "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.Status",
           "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.ConnectionType",
           "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.ExternalIPAddress",
           "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.DNSEnabled",
           "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.DNSServers",
           "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.Enable",
           "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.LastConnectionError",
           "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.Username",
           "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.TransportType",
           "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.MACAddress",
           "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.ConnectionStatus",
           "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.NATEnabled",
           "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.Uptime"]

wan_pots = ["InternetGatewayDevice.WANDevice.1.WANConnectionDevice._x_.WANPOTSLinkConfig.Enable",
            "InternetGatewayDevice.WANDevice.1.WANConnectionDevice._x_.WANPOTSLinkConfig.DataCompression",
            "InternetGatewayDevice.WANDevice.1.WANConnectionDevice._x_.WANPOTSLinkConfig.DataModulationSupported",
            "InternetGatewayDevice.WANDevice.1.WANConnectionDevice._x_.WANPOTSLinkConfig.DataProtocol",
            "InternetGatewayDevice.WANDevice.1.WANConnectionDevice._x_.WANPOTSLinkConfig.DelayBetweenRetries",
            "InternetGatewayDevice.WANDevice.1.WANConnectionDevice._x_.WANPOTSLinkConfig.Fclass",
            "InternetGatewayDevice.WANDevice.1.WANConnectionDevice._x_.WANPOTSLinkConfig.ISPInfo",
            "InternetGatewayDevice.WANDevice.1.WANConnectionDevice._x_.WANPOTSLinkConfig.ISPPhoneNumber",
            "InternetGatewayDevice.WANDevice.1.WANConnectionDevice._x_.WANPOTSLinkConfig.LinkStatus",
            "InternetGatewayDevice.WANDevice.1.WANConnectionDevice._x_.WANPOTSLinkConfig.LinkType",
            "InternetGatewayDevice.WANDevice.1.WANConnectionDevice._x_.WANPOTSLinkConfig.PlusVTRCommandSupported"]

wan_dsl_link = ["InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANDSLLinkConfig._x_.Enable",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANDSLLinkConfig._x_.AAL5CRCErrors",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANDSLLinkConfig._x_.ATMAAL",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANDSLLinkConfig._x_.ATMCRCErrors",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANDSLLinkConfig._x_.ATMEncapsulation",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANDSLLinkConfig._x_.ATMHECErrors",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANDSLLinkConfig._x_.ATMMaximumBurstSize",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANDSLLinkConfig._x_.ATMPeakCellRate",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANDSLLinkConfig._x_.ATMQoS",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANDSLLinkConfig._x_.ATMReceivedBlocks",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANDSLLinkConfig._x_.ATMSustainableCellRate",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANDSLLinkConfig._x_.ATMTransmittedBlocks",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANDSLLinkConfig._x_.DestinationAddress",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANDSLLinkConfig._x_.LinkStatus",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANDSLLinkConfig._x_.LinkType",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANDSLLinkConfig._x_.ModulationType"]

wan_ip_stats = ["InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.Name",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.MACAddress",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.Stats.EthernetBytesReceived",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.Stats.EthernetBytesSent",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.Stats.EthernetDiscardPacketsReceived",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.Stats.EthernetDiscardPacketsSent",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.Stats.EthernetErrorsReceived",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.Stats.EthernetErrorsSent",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.Stats.EthernetMulticastPacketsReceived",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.Stats.EthernetMulticastPacketsSent",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.Stats.EthernetPacketsReceived",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.Stats.EthernetPacketsSent",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.Stats.EthernetUnicastPacketsReceived",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.Stats.EthernetUnicastPacketsSent",
                "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.Stats.EthernetUnknownProtoPacketsReceived"]

wan_ppp_stats = [
                 "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.Stats.EthernetBytesReceived",
                 "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.Stats.EthernetBytesSent",
                 "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.Stats.EthernetDiscardPacketsReceived",
                 "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.Stats.EthernetDiscardPacketsSent",
                 "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.Stats.EthernetErrorsReceived",
                 "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.Stats.EthernetErrorsSent",
                 "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.Stats.EthernetMulticastPacketsReceived",
                 "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.Stats.EthernetMulticastPacketsSent",
                 "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.Stats.EthernetPacketsReceived",
                 "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.Stats.EthernetPacketsSent",
                 "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.Stats.EthernetUnicastPacketsReceived",
                 "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.Stats.EthernetUnicastPacketsSent",
                 "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.Stats.EthernetUnknownProtoPacketsReceived"
                 ]

wan_common_stats = ["InternetGatewayDevice.WANDevice._x_.WANCommonInterfaceConfig.TotalBytesReceived",
                    "InternetGatewayDevice.WANDevice._x_.WANCommonInterfaceConfig.TotalBytesSent",
                    "InternetGatewayDevice.WANDevice._x_.WANCommonInterfaceConfig.TotalPacketsReceived",
                    "InternetGatewayDevice.WANDevice._x_.WANCommonInterfaceConfig.TotalPacketsSent",
                    "InternetGatewayDevice.WANDevice._x_.WANCommonInterfaceConfig.EnabledForInternet",
                    "InternetGatewayDevice.WANDevice._x_.WANCommonInterfaceConfig.Layer1DownstreamMaxBitRate",
                    "InternetGatewayDevice.WANDevice._x_.WANCommonInterfaceConfig.Layer1UpstreamMaxBitRate",
                    "InternetGatewayDevice.WANDevice._x_.WANCommonInterfaceConfig.PhysicalLinkStatus",
                    "InternetGatewayDevice.WANDevice._x_.WANCommonInterfaceConfig.WANAccessType"]

wan_eth_stats = ["InternetGatewayDevice.WANDevice._x_.WANEthernetInterfaceConfig.Status",
                 "InternetGatewayDevice.WANDevice._x_.WANEthernetInterfaceConfig.MACAddress",
                 "InternetGatewayDevice.WANDevice._x_.WANEthernetInterfaceConfig.DuplexMode",
                 "InternetGatewayDevice.WANDevice._x_.WANEthernetInterfaceConfig.Stats.BytesReceived",
                 "InternetGatewayDevice.WANDevice._x_.WANEthernetInterfaceConfig.Stats.BytesSent",
                 "InternetGatewayDevice.WANDevice._x_.WANEthernetInterfaceConfig.Stats.PacketsReceived",
                 "InternetGatewayDevice.WANDevice._x_.WANEthernetInterfaceConfig.Stats.PacketsSent",
                 "InternetGatewayDevice.WANDevice._x_.WANEthernetInterfaceConfig.MaxBitRate"]

port_mapPPP = ["InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection.1.PortMapping._x_.PortMappingEnabled",
            "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection.1.PortMapping._x_.PortMappingDescription",
            "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection.1.PortMapping._x_.PortMappingProtocol",
            "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection.1.PortMapping._x_.ExternalPort",
            "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection.1.PortMapping._x_.InternalClient",
            "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection.1.PortMapping._x_.InternalPort"]

port_mapPPP_y = ["InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.PortMapping.1.PortMappingEnabled",
            "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.PortMapping.1.PortMappingDescription",
            "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.PortMapping.1.PortMappingProtocol",
            "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.PortMapping.1.ExternalPort",
            "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.PortMapping.1.InternalClient",
            "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.PortMapping.1.InternalPort"]

port_mapIP = ["InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection.1.PortMapping._x_.PortMappingEnabled",
            "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection.1.PortMapping._x_.PortMappingDescription",
            "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection.1.PortMapping._x_.PortMappingProtocol",
            "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection.1.PortMapping._x_.ExternalPort",
            "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection.1.PortMapping._x_.InternalClient",
            "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection.1.PortMapping._x_.InternalPort"]


nat_info = ["InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.DHCPServerEnable",
            "InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.IPInterface.1.IPInterfaceAddressingType",
            "InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.IPInterface.1.IPInterfaceIPAddress",
            "InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.IPInterface.2.IPInterfaceAddressingType",
            "InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.IPInterface.2.IPInterfaceIPAddress",
            "InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.IPInterface.3.IPInterfaceAddressingType",
            "InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.IPInterface.3.IPInterfaceIPAddress",
            "InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.IPInterface.4.IPInterfaceAddressingType",
            "InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.IPInterface.4.IPInterfaceIPAddress",
            "InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.IPRouters",
            "InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.MaxAddress",
            "InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.MinAddress",
            "InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.SubnetMask",
            "InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.DHCPLeaseTime"]

serving_pool = ["InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.DHCPConditionalServingPool._x_.DHCPLeaseTime",
                "InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.DHCPConditionalServingPool._x_.DHCPStaticAddress.1.Chaddr",
                "InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.DHCPConditionalServingPool._x_.DNSServers",
                "InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.DHCPConditionalServingPool._x_.Enable",
                "InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.DHCPConditionalServingPool._x_.IPRouters",
                "InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.DHCPConditionalServingPool._x_.MaxAddress",
                "InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.DHCPConditionalServingPool._x_.MinAddress",
                "InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.DHCPConditionalServingPool._x_.SubnetMask"]

lan_ports = ["InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig._x_.Name",
             "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig._x_.Status",
             "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig._x_.Enable",
             "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig._x_.DuplexMode",
             "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig._x_.MaxBitRate",
             "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig._x_.Stats.BytesReceived",
             "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig._x_.Stats.BytesSent",
             "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig._x_.Stats.PacketsReceived",
             "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig._x_.Stats.BroadcastPacketsReceived",
             "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig._x_.Stats.DiscardPacketsReceived",
             "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig._x_.Stats.ErrorsReceived",
             "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig._x_.Stats.MulticastPacketsReceived",
             "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig._x_.Stats.UnicastPacketsReceived",
             "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig._x_.Stats.PacketsSent",
             "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.Stats.BroadcastPacketsSent",
             "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.Stats.DiscardPacketsSent",
             "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.Stats.ErrorsSent",
             "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.Stats.MulticastPacketsSent",
             "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.Stats.UnicastPacketsSent"
]

wifi = ["InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.Name",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.Enable",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.Status",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.BasicAuthenticationMode",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.BasicEncryptionModes",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.IEEE11iAuthenticationMode",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.IEEE11iEncryptionModes",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.RegulatoryDomain",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.WPS.Enable",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.WPAAuthenticationMode",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.WPAEncryptionModes",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.SSID",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.BSSID",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.Standard",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.BeaconType",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.MaxBitRate",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.Channel",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.TotalAssociations",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.TransmitPower",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.WMMEnable",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.TotalBytesReceived",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.TotalBytesSent",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.TotalPacketsReceived",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.Stats.BroadcastPacketsReceived",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.Stats.DiscardPacketsReceived",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.Stats.ErrorsReceived",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.Stats.MulticastPacketsReceived",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.Stats.UnicastPacketsReceived",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.Stats.UnknownProtoPacketsReceived",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.TotalPacketsSent",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.Stats.BroadcastPacketsSent",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.Stats.DiscardPacketsSent",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.Stats.ErrorsSent",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.Stats.MulticastPacketsSent",
        "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.Stats.UnicastPacketsSent"
        ]
wadsl = ["InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Status",
         "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.DownstreamAttenuation",
         "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.DownstreamCurrRate",
         "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.DownstreamMaxRate",
         "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.DownstreamNoiseMargin",
         "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.DownstreamPower",
         "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.UpstreamAttenuation",
         "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.UpstreamCurrRate",
         "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.UpstreamMaxRate",
         "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.UpstreamNoiseMargin",
         "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.UpstreamPower",
         "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.LineEncoding",
         "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.ModulationType",
         "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.Total.ATUCCRCErrors",
         "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.Total.ATUCFECErrors",
         "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.Total.CRCErrors",
         "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.Total.CellDelin",
         "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.Total.FECErrors",
         "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.Total.HECErrors",
         "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.Total.InitErrors",
         "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.Total.InitTimeouts",
         "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.Total.ReceiveBlocks",
         "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.Total.TransmitBlocks"

         ]

dsl_stats = ["InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.Showtime.ATUCCRCErrors",
             "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.Showtime.ATUCFECErrors",
             "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.Showtime.CRCErrors",
             "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.Showtime.CellDelin",
             "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.Showtime.FECErrors",
             "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.Showtime.HECErrors",
             "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.Showtime.InitErrors",
             "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.Showtime.InitTimeouts",
             "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.Showtime.ReceiveBlocks",
             "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.Showtime.TransmitBlocks"]

DSL_CD_Stats = ["InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.CurrentDay.CRCErrors",
                "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.CurrentDay.CellDelin",
                "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.CurrentDay.FECErrors",
                "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.CurrentDay.ErroredSecs",
                "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.CurrentDay.InitErrors",
                "InternetGatewayDevice.WANDevice._x_.WANDSLInterfaceConfig.Stats.QuarterHour.CRCErrors"]

trace_roat = ["InternetGatewayDevice.Layer3Forwarding.Forwarding._x_.Status",
              "InternetGatewayDevice.Layer3Forwarding.Forwarding._x_.DestIPAddress",
              "InternetGatewayDevice.Layer3Forwarding.Forwarding._x_.DestSubnetMask",
              "InternetGatewayDevice.Layer3Forwarding.Forwarding._x_.ForwardingMetric",
              "InternetGatewayDevice.Layer3Forwarding.Forwarding._x_.GatewayIPAddress",
              "InternetGatewayDevice.Layer3Forwarding.Forwarding._x_.SourceIPAddress",
              "InternetGatewayDevice.Layer3Forwarding.Forwarding._x_.SourceSubnetMask",
              "InternetGatewayDevice.Layer3Forwarding.Forwarding._x_.Interface",
              "InternetGatewayDevice.Layer3Forwarding.Forwarding._x_.StaticRoute"]

user_interface = ["InternetGatewayDevice.UserInterface.ISPHelpDesk",
                  "InternetGatewayDevice.UserInterface.ISPHelpPage",
                  "InternetGatewayDevice.UserInterface.ISPHomePage",
                  "InternetGatewayDevice.UserInterface.ISPLogo",
                  "InternetGatewayDevice.UserInterface.ISPMailServer",
                  "InternetGatewayDevice.UserInterface.ISPNewsServer",
                  "InternetGatewayDevice.UserInterface.UserDatabaseSupported",
                  "InternetGatewayDevice.UserInterface.UserUpdateServer",
                  "InternetGatewayDevice.UserInterface.WarrantyDate",
                  "InternetGatewayDevice.UserInterface.CurrentLanguage",
                  "InternetGatewayDevice.UserInterface.ExampleLogin",
                  "InternetGatewayDevice.UserInterface.ExamplePassword",
                  "InternetGatewayDevice.UserInterface.RemoteAccess.Enable",
                  "InternetGatewayDevice.UserInterface.RemoteAccess.Port",
                  "InternetGatewayDevice.UserInterface.RemoteAccess.Protocol"]