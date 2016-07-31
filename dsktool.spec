Summary:	Diskette tools - GUI front-end to LibDsk
Summary(pl.UTF-8):	Narzędzia do dyskietek - graficzny interfejs do LibDsk
Name:		dsktool
Version:	1.0.5
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://www.seasip.info/Unix/LibDsk/%{name}-%{version}.tar.gz
# Source0-md5:	6cb3b6ebb11b7e7102976c26a7ec8c3f
URL:		http://www.seasip.info/Unix/LibDsk/#tools
BuildRequires:	libdsk-devel
BuildRequires:	rpmbuild(macros) >= 1.167
BuildRequires:	wxGTK2-devel >= 2.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Diskette Tools program is a GUI front-end to LibDsk. It doesn't do
any more than the provided sample utilities, but it looks nicer.

%description -l pl.UTF-8
Program Diskette Tools to graficzny interfejs użytkownika do LibDsk.
Nie robi więcej niż załączone programy przykładowe, ale wygląda
przyjemniej.

%prep
%setup -q

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags} `wx-gtk2-ansi-config --cflags`" \
	WX_LIBS="`wx-gtk2-ansi-config --libs`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	INSTALLDIR=$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_bindir}/dsktool
