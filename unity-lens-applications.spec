Name:		unity-lens-applications
Version:	0.4.12
Release:	1
License:	GPLv3
Summary:	Application lens for the Unity Desktop
Url:		https://launchpad.net/unity-lens-applications
Group:		Graphical desktop/Other
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	intltool
BuildRequires:	pkgconfig(dee-1.0)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gee-1.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libgnome-menu)
BuildRequires:	pkgconfig(unity)
BuildRequires:	pkgconfig(zeitgeist-1.0)
# #error "unity-lens-applications only compiles and works against libdb-4.8.
BuildRequires:	db4-devel
BuildRequires:	vala-devel
BuildRequires:	libxapian-devel

%description
This package contains the "application" lens which can be used
into Unity to launch and install applications.


%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog COPYING
%dir %{_datadir}/unity
%dir %{_datadir}/unity/themes
%config %{_sysconfdir}/xdg/menus/unity-lens-applications.menu
%{_libdir}/unity-applications-daemon
%{_datadir}/dbus-1/services/unity-lens-applications.service
%{_datadir}/unity/lenses/
%{_datadir}/unity/themes/applications.png
%{_datadir}/desktop-directories/X-Unity-All-Applications.directory
