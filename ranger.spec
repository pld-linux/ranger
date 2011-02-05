Summary:	A simple, vim-like file manager
Summary(hu.UTF-8):	Egyszerű, vim-szerű fájlkezelő
Name:		ranger
Version:	1.4.1
Release:	0.1
License:	GPL v3
Group:		Applications/Shells
Source0:	http://download.savannah.gnu.org/releases/ranger/releases/%{name}-%{version}.tar.gz
# Source0-md5:	b59eefde55fdf65b2a7599f9d8ac0632
URL:		http://savannah.nongnu.org/projects/ranger/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple, vim-like file manager.

%description -l hu.UTF-8
Egyszerű, vim-szerű fájlkezelő.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/ranger-1.4.1-py2.7.egg-info
%endif
%{py_sitescriptdir}/ranger
%{_mandir}/man1/ranger*
