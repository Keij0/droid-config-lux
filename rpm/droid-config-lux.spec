# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc

%define device lux
%define vendor motorola

%define vendor_pretty Motorola
%define device_pretty Moto X Play

# Adjust this for your device
%define pixel_ratio 1.5

%define ofono_enable_plugins bluez5,hfp_ag_bluez5

%define ofono_disable_plugins bluez4,dun_gw_bluez4,hfp_ag_bluez4,hfp_bluez4,dun_gw_bluez5,hfp_bluez5

# Community HW adaptations need this
%define community_adaptation 1

Provides: ofono-configs
Obsoletes: ofono-configs-mer

%include droid-configs-device/droid-configs.inc
