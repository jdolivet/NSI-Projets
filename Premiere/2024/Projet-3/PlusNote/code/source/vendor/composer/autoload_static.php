<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInit87c57847cf8e703e95b5bbdfa1a23f91
{
    public static $prefixLengthsPsr4 = array (
        'P' => 
        array (
            'PHPMailer\\PHPMailer\\' => 20,
        ),
    );

    public static $prefixDirsPsr4 = array (
        'PHPMailer\\PHPMailer\\' => 
        array (
            0 => __DIR__ . '/..' . '/phpmailer/phpmailer/src',
        ),
    );

    public static $classMap = array (
        'Composer\\InstalledVersions' => __DIR__ . '/..' . '/composer/InstalledVersions.php',
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->prefixLengthsPsr4 = ComposerStaticInit87c57847cf8e703e95b5bbdfa1a23f91::$prefixLengthsPsr4;
            $loader->prefixDirsPsr4 = ComposerStaticInit87c57847cf8e703e95b5bbdfa1a23f91::$prefixDirsPsr4;
            $loader->classMap = ComposerStaticInit87c57847cf8e703e95b5bbdfa1a23f91::$classMap;

        }, null, ClassLoader::class);
    }
}
