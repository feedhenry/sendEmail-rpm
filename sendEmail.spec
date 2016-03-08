Name: sendEmail
Version: 1.56
Release: 1%{?dist}
Summary:  An Email program for sending SMTP mail from a command line

License: GPLv2+
URL: http://caspian.dotconf.net/menu/Software/SendEmail/
BuildArch: noarch

Source0: http://caspian.dotconf.net/menu/Software/SendEmail/%{name}-v%{version}.tar.gz

# Remove explicit setting of SSL version
# http://unix.stackexchange.com/a/258820/86764
Patch0: %{name}-remove-ssl-version.patch


%description
SendEmail is a lightweight, command line SMTP email client. If you
have the need to send email from a command line, this free program is
perfect: simple to use and feature rich. It was designed to be used in
bash scripts, batch files, Perl programs and web sites, but is quite
adaptable and will likely meet your requirements. SendEmail is written
in Perl and is unique in that it requires NO MODULES. It has an
intuitive and flexible set of command-line options, making it very
easy to learn and use.

%prep
%setup -q -n %{name}-v%{version}

%patch0 -p1

%build
# nothing to do

%install
%{__install} -d %{buildroot}%{_bindir}/
%{__install} -m 0755 -p %{name} %{buildroot}%{_bindir}/
ln -s %{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}.pl

%files
%{_bindir}/%{name}
%{_bindir}/%{name}.pl
%doc CHANGELOG README TODO

%changelog
* Mon Mar  7 2016 Gerard Ryan <gerard@ryan.lt> - 1.56-1
- Initial spec file creation

