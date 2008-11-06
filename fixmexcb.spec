%include	/usr/lib/rpm/macros.perl
Summary:	Pakages converter (tgz, rpm, deb, slp)
Summary(pl.UTF-8):	Konwerter pakietów (tgz, rpm, deb, slp)
Name:		fixmexcb
Version:	0.1
Release:	1
License:	GPL
Group:		Applications/System
URL:		http://kitenet.net/programs/alien/
Provides:	libtool(/usr/lib/libxcb-xlib.la)
Provides:	libtool(/usr/lib64/libxcb-xlib.la)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alien allows you to convert Debian, Stampede and Slackware Packages
into PLD packages, which can be installed with rpm. It can also
convert into Slackware, Debian, and Stampede packages. This is a tool
only suitable for binary packages.

%description -l pl.UTF-8
Alien pozwala przekonwertować pakiety Debiana, Stampede oraz Slackware
w pakiety używane w PLD, które mogą być zainstalowane przy użyciu
rpm-a i odwrotnie. Narzędzie to jest przydatne wyłącznie dla pakietów
binarnych.

%prep
%setup -q -c -T

%build

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
